
# 🌍 Tunisian Tourist Destination Recommendation System

![GitHub stars](https://img.shields.io/github/stars/kerfaiyass54/spatial-computing-project?style=social)
![GitHub forks](https://img.shields.io/github/forks/kerfaiyass54/spatial-computing-project?style=social)
![GitHub issues](https://img.shields.io/github/issues/kerfaiyass54/spatial-computing-project)
![GitHub license](https://img.shields.io/github/license/kerfaiyass54/spatial-computing-project)

**A data-driven, AI-powered recommendation system for discovering Tunisia's hidden gems and iconic landmarks through geospatial analysis and visual storytelling.**

---

## ✨ Features

✅ **Geospatial Analysis** – Analyze thousands of tourist photos to identify popular destinations
✅ **Interactive Map Visualization** – Explore Tunisia with an interactive map showing hotspots
✅ **AI-Generated Travel Guides** – Get rich, descriptive guides for each location using advanced NLP
✅ **Historical & Cultural Insights** – Discover Tunisia's rich heritage through curated content
✅ **Multi-Modal Recommendations** – Combine visual data with textual descriptions for comprehensive insights
✅ **OpenStreetMap Integration** – Detailed maps with routes to popular destinations

---

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.8+** – Primary programming language
- **Flask** – Web framework for the backend
- **Pandas** – Data manipulation and analysis
- **Scikit-learn** – Machine learning for clustering and recommendations
- **Cartopy** – Advanced geospatial visualization
- **OpenStreetMap** – Base map data
- **Leaflet.js** – Interactive map frontend

### AI/ML Components
- **GPT-2** – Text generation for travel guides
- **CLIP Model** – Image-text alignment for visual recommendations
- **DBSCAN/OPTICS** – Density-based clustering for hotspot detection

### Data Sources
- **Flickr API** – Geotagged tourist photos
- **CSV Data** – Processed geospatial data
- **Open Data Portals** – Additional location information

---

## 📦 Installation

### Prerequisites

Before you begin, ensure you have:
- Python 3.8 or higher
- pip package manager
- A Flickr API key (for data collection)
- Basic knowledge of Python and Flask

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/kerfaiyass54/spatial-computing-project.git
   cd spatial-computing-project
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root with your Flickr API credentials:
   ```
   FLICKR_API_KEY=your_api_key_here
   FLICKR_API_SECRET=your_api_secret_here
   ```

5. **Download the dataset:**
   ```bash
   python main.py --download
   ```

6. **Run the application:**
   ```bash
   python webapp.py
   ```

7. **Access the application:**
   Open your browser to `http://localhost:5000`

---


## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root with these variables:
```
FLICKR_API_KEY=your_api_key
FLICKR_API_SECRET=your_api_secret
MAP_ZOOM_LEVEL=12
MAP_CENTER_LAT=33.8869
MAP_CENTER_LON=9.5375
```

### Customization Options

1. **Map Settings:**
   Modify the center coordinates and zoom level in `webapp.py`:
   ```python
   map = L.map('map').setView([33.8869, 9.5375], 12)
   ```

2. **Recommendation Parameters:**
   Adjust the clustering algorithm parameters in `mapping.py`:
   ```python
   # Example parameters for DBSCAN
   eps = 0.005  # Distance threshold
   min_samples = 5  # Minimum points to form a cluster
   ```

3. **AI Model Configuration:**
   Modify the text generation parameters in `recommendation.py`:
   ```python
   output = gpt2_model.generate(
       input_ids,
       max_length=150,
       num_beams=5,
       no_repeat_ngram_size=2
   )
   ```

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### How to Contribute

1. **Fork the repository** and create your branch from `main`.
2. **Write tests** for your changes.
3. **Document your changes** in the code and update the README.
4. **Submit a pull request** with a clear description of your changes.

### Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/kerfaiyass54/spatial-computing-project.git
   cd spatial-computing-project
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

3. Run tests:
   ```bash
   pytest tests/
   ```

### Code Style Guidelines

- Follow **PEP 8** style guidelines
- Use **type hints** for all functions
- Write **docstrings** for all modules and functions
- Keep functions **modular** and **reusable**

### Pull Request Process

1. Ensure your code passes all tests
2. Update the documentation
3. Submit a clear description of your changes
4. Reference any related issues

---



### FAQ

**Q: How accurate are the recommendations?**
A: The system uses geospatial clustering and AI-generated descriptions. Accuracy depends on the quality and quantity of available data.

**Q: Can I use this for commercial purposes?**
A: Yes, under the MIT License. However, ensure you comply with Flickr's terms of service regarding data usage.

**Q: How can I add more locations?**
A: Add geotagged photos to your dataset and run the data processing script to update the recommendations.



## 🚀 Get Started Today!

Ready to explore Tunisia's hidden gems? Clone the repository, set up your environment, and dive into the code:

```bash
git clone https://github.com/kerfaiyass54/spatial-computing-project.git
cd spatial-computing-project
python webapp.py
```

Visit `http://localhost:5000` to start your journey!


