#!/usr/bin/env python3
"""
Scrape apartment pages from beimlenzer.de and download images + extract text.

Usage:
  python scripts/scrape_beimlenzer.py

Outputs:
  - Saves images into assets/<name>/ with sequential filenames
  - Creates apartment data for app.js

Notes:
  - For personal migration/backup. Respect robots.txt and TOS. Do not abuse.
"""
import json
import os
import re
import sys
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
}

BASE_URL = "https://www.beimlenzer.de/"
IMG_EXT_ALLOW = {".jpg", ".jpeg", ".png", ".webp"}

def sanitize_filename(name: str) -> str:
    name = name.strip().lower()
    name = re.sub(r"[^a-z0-9-_]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name or "images"

def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)

def download_image(url: str, output_path: str) -> bool:
    try:
        response = requests.get(url, headers=HEADERS, stream=True, timeout=30)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"Downloaded: {output_path}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def scrape_main_page():
    """Scrape the main beimlenzer.de page for general info and images"""
    try:
        response = requests.get(BASE_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Create assets directory
        assets_dir = "assets/main"
        ensure_dir(assets_dir)
        
        # Find and download images
        images = soup.find_all('img')
        downloaded_images = []
        
        for i, img in enumerate(images, 1):
            src = img.get('src')
            if not src:
                continue
                
            # Convert relative URLs to absolute
            if src.startswith('/'):
                img_url = urljoin(BASE_URL, src)
            elif not src.startswith('http'):
                img_url = urljoin(BASE_URL, src)
            else:
                img_url = src
            
            # Check if it's an image we want
            parsed_url = urlparse(img_url)
            if any(parsed_url.path.lower().endswith(ext) for ext in IMG_EXT_ALLOW):
                filename = f"img-{i:02d}.jpg"
                output_path = os.path.join(assets_dir, filename)
                
                if download_image(img_url, output_path):
                    downloaded_images.append({
                        "src": f"assets/main/{filename}",
                        "alt": img.get('alt', f"Beim Lenzer - Image {i}")
                    })
        
        # Extract text content
        title = soup.find('title')
        title_text = title.text.strip() if title else "Ferienhaus Beim Lenzer"
        
        # Look for description or main content
        description = ""
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            description = meta_desc.get('content', '')
        
        metadata = {
            "title": title_text,
            "description": description,
            "images": downloaded_images,
            "source_url": BASE_URL
        }
        
        # Save metadata
        with open(os.path.join(assets_dir, "metadata.json"), 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"Scraped {len(downloaded_images)} images from main page")
        return metadata
        
    except Exception as e:
        print(f"Error scraping main page: {e}")
        return None

if __name__ == "__main__":
    print("Scraping beimlenzer.de...")
    metadata = scrape_main_page()
    if metadata:
        print("Scraping completed successfully!")
        print(f"Title: {metadata['title']}")
        print(f"Description: {metadata['description']}")
        print(f"Images downloaded: {len(metadata['images'])}")
    else:
        print("Scraping failed!")
        sys.exit(1)