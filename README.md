# Tunisian Tourist Destination Recommendation System

## Introduction
This project is a **recommendation system prototype** for Tunisian tourist destinations, built using Python and geospatial tools. It helps users discover tourist attractions by leveraging geospatial data and providing map-based recommendations.

---

## Features
- Recommend tourist destinations across Tunisia based on user preferences and proximity.
- Visualize recommendations on an interactive map using geospatial tools.
- Filter results by category (e.g., historical landmarks, beaches, mountains).
- Real-time geolocation support for nearby recommendations.

---

## Files Descriptions

- `main.py`, `webapp.py`: Main application file containing the backend logic.
- `templates/`: Contains HTML files for the user interface.
  - `index.html`: Displays the map and recommendations.
- `static/`: Holds CSS, JavaScript, and images for styling and interactivity.
  - `style.css`: Styles for the web interface.
  - `map.js`: JavaScript for rendering and interacting with the map.
- `CSV/` and `IMG/`: Contains geospatial data files.
- `recommandation.py` and `mapping.py`: Use pcitures to do the poiting on the map.  

---

## How to Upload and Run It

### Prerequisites
1. Install Python 3.x.
2. Install the required Python libraries.

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/kerfaiyass54/spatial-computing-project.git
   cd tunisian-tourist-recommender

2. Install dependencies:
   ```bash
   pip install + libname


3. Run the application:
   ```bash
   python webapp.py

4. Consult the application:
   ```bash
   localhost:5000
  
