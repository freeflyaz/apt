# Apartment Rental Websites Collection

This repository contains vacation rental websites built using modern web technologies and automated content gathering.

## Project Overview

A collection of apartment rental websites, starting with the **Beimlenzer** vacation rental site in Schwangau, Bavaria, Germany.

## Beimlenzer Project

### What We Built

A complete vacation rental booking website featuring:
- **3 Premium Apartments**: Säuling, Branderschrofen, and Geiselstein
- **26 High-Quality Images** scraped and downloaded from the original beimlenzer.de website
- **Full Booking System** with pricing calculations and email integration
- **Interactive Photo Gallery** with filtering by apartment
- **Bilingual Support** (German/English)
- **Modern Responsive Design**

### Technical Implementation

#### 1. **MCP (Model Context Protocol) Web Scraping**
- Used Playwright MCP to navigate and scrape https://www.beimlenzer.de/ferienwohnungen/fewo-saeuling
- Identified 7 available apartments, selected the best 3 for our site
- Automated image URL extraction and download process
- Downloaded 26 images totaling ~7MB with proper naming conventions

#### 2. **Template Adaptation Process**
1. **Started with existing template** - Had a base vacation rental website template
2. **Created new project folder** - Copied template into `beimlenzer/` directory 
3. **Updated apartment configuration** - Replaced template apartments with real data from beimlenzer.de
4. **Organized assets** - Structured images in `assets/[apartment-name]/` directories
5. **Fixed gallery system** - Updated filter buttons and "View photos" functionality
6. **Cleaned UI** - Removed repetitive apartment name labels for better user experience

#### 3. **Apartment Data Integration**

**Säuling** (€95-120/night)
- 70m², sleeps 4, 2 bedrooms + living room
- 9 photos: living room, kitchen, dining area, 2 bedrooms, 2 bathrooms, balcony view, floor plan

**Branderschrofen** (€105-130/night) 
- 80m², sleeps 4, 2 bedrooms + living room
- 9 photos: seating area, kitchen, 2 bedrooms, bathroom, 3 balcony views, house exterior, floor plan

**Geiselstein** (€85-110/night)
- 60m², sleeps 4, 2 bedrooms + living room  
- 7 photos: living room, kitchen combo, 2 bedrooms, bathroom, balcony view, floor plan

### Key Features

- **Dynamic Pricing**: Different rates for high/low seasons
- **Booking Calculator**: Real-time price calculation with cleaning fees
- **Email Integration**: EmailJS for booking requests with fallback to mailto
- **Gallery Filtering**: Filter photos by apartment or view all
- **Lightbox Viewer**: Full-screen photo viewing with navigation
- **Mobile Responsive**: Optimized for all device sizes
- **SEO Optimized**: Proper meta tags and structured data

### File Structure

```
beimlenzer/
├── index.html              # Main website file
├── app.js                  # Core functionality and apartment data
├── styles.css              # Styling and responsive design
├── emailjs-template.html   # Email template for booking requests
└── assets/
    ├── saeuling/           # Säuling apartment photos (9 images)
    ├── branderschrofen/    # Branderschrofen apartment photos (9 images)
    ├── geiselstein/        # Geiselstein apartment photos (7 images)
    └── seestadel/          # Legacy template images (4 images)
```

### Technologies Used

- **Frontend**: Vanilla HTML5, CSS3, JavaScript (ES6+)
- **Calendar**: Flatpickr for date selection
- **Email**: EmailJS for booking form submissions
- **Analytics**: GoatCounter for privacy-friendly visitor tracking
- **Fonts**: Google Fonts (Inter, Playfair Display)
- **Automation**: Playwright MCP for web scraping
- **Version Control**: Git with GitHub hosting

### Development Workflow

1. **Content Gathering**: Use MCP/Playwright to scrape apartment data and images
2. **Template Setup**: Copy base template to new project directory
3. **Data Integration**: Update apartment configurations with real data
4. **Asset Organization**: Structure images in logical directory hierarchy  
5. **Feature Implementation**: Build booking system, gallery, and responsive design
6. **Testing & Refinement**: Test functionality and improve user experience
7. **Deployment**: Commit to Git and deploy to hosting platform

### Getting Started

1. Clone the repository:
```bash
git clone https://github.com/freeflyaz/apt.git
cd apt/beimlenzer
```

2. Start a local server:
```bash
python3 -m http.server 8000
# or
npx serve .
```

3. Open http://localhost:8000 in your browser

### Future Enhancements

- Add more apartment locations
- Implement availability calendar
- Add payment processing integration
- Create admin dashboard for content management
- Add multi-language support for more regions

---

**Built with Claude Code** 🤖  
*Automated web scraping and development workflow*