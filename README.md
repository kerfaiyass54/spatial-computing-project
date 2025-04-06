# Tunisian Tourist Destination Recommendation System

## Introduction
This project is a **recommendation system prototype** for Tunisian tourist destinations, done by me and my colleague and built using Python and geospatial tools. It helps users discover tourist attractions by leveraging geospatial data and providing map-based recommendations.

---

## Features
- Recommend tourist destinations across Tunisia based on geospatial data.
- Visualize recommendations on an interactive map using geospatial tools.
- Show the full roads towards those recommandations.
- Give a full Tunisian map.

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

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

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
  
