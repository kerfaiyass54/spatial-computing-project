
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

## 🎯 Usage

### Basic Usage

#### Exploring the Map Interface
1. Navigate to `http://localhost:5000` in your browser
2. View the interactive map showing popular tourist destinations
3. Click on markers to see detailed information about each location

#### Generating Travel Guides
```python
# Example of how to generate a travel guide programmatically
from recommendation import generate_travel_guide

location_data = {
    "name": "Sidi Bou Said",
    "latitude": 36.870858,
    "longitude": 10.346009
}

guide = generate_travel_guide(location_data)
print(guide)
```

#### Running Data Analysis
```bash
# Process geospatial data and generate visualizations
python mapping.py --process
```

### Advanced Usage

#### Customizing the Recommendation Algorithm
Modify the clustering parameters in `mapping.py`:
```python
# Example of adjusting DBSCAN parameters
from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps=0.005, min_samples=5)  # Adjust eps and min_samples
```

#### Adding New Data Sources
To incorporate additional data sources:
1. Add the data to your `CSV/` directory
2. Update the data processing pipeline in `main.py`
3. Modify the visualization scripts in `mapping.py`

---

## 📁 Project Structure

```
spatial-computing-project/
│
├── .env                  # Environment variables
├── README.md             # Project documentation
├── requirements.txt       # Python dependencies
│
├── src/
│   ├── main.py           # Data collection and processing
│   ├── recommendation.py  # AI recommendation engine
│   ├── mapping.py        # Geospatial visualization
│   └── webapp.py         # Flask web application
│
├── templates/
│   └── index.html        # Frontend template
│
├── static/
│   ├── style.css         # CSS styles
│   └── map.js           # Map interaction scripts
│
├── CSV/
│   └── dirty.csv         # Raw geospatial data
│
├── IMG/
│   └── ...               # Image assets
│
└── getinfo/              # Flickr photo metadata
```

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

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors & Contributors

**Project Lead:**
[@kerfaiyass54](https://github.com/kerfaiyass54)

**Contributors:**
- [@yourusername](https://github.com/yourusername)
- [@anothercontributor](https://github.com/anothercontributor)

**Special Thanks:**
- Flickr API team for providing geotagged data
- OpenStreetMap community for map data
- All contributors for their valuable feedback

---

## 🐛 Issues & Support

### Reporting Issues

If you encounter any problems or have feature requests:
1. Check the [GitHub Issues](https://github.com/kerfaiyass54/spatial-computing-project/issues) for existing issues
2. Open a new issue with a clear description and steps to reproduce

### Getting Help

- **Discussions:** Join our [GitHub Discussions](https://github.com/kerfaiyass54/spatial-computing-project/discussions)
- **Community:** Find us on [Twitter](https://twitter.com/yourhandle)
- **Email:** contact@yourdomain.com

### FAQ

**Q: How accurate are the recommendations?**
A: The system uses geospatial clustering and AI-generated descriptions. Accuracy depends on the quality and quantity of available data.

**Q: Can I use this for commercial purposes?**
A: Yes, under the MIT License. However, ensure you comply with Flickr's terms of service regarding data usage.

**Q: How can I add more locations?**
A: Add geotagged photos to your dataset and run the data processing script to update the recommendations.

---

## 🗺️ Roadmap

### Planned Features

- **Enhanced AI Models:** Implement more advanced NLP models for richer travel guides
- **User Personalization:** Allow users to save favorite destinations and get personalized recommendations
- **Mobile App:** Develop a companion mobile application
- **AR Integration:** Augmented reality features for exploring locations
- **More Data Sources:** Incorporate additional platforms like Instagram and Google Maps

### Known Issues

- **API Rate Limits:** Flickr API has rate limits that may affect data collection
- **Map Performance:** Large datasets may impact map rendering performance
- **Data Freshness:** Recommendations are based on historical data (2017-2019)

### Future Improvements

- **Real-time Data:** Incorporate real-time data sources for up-to-date recommendations
- **Community Contributions:** Allow users to contribute their own photos and recommendations
- **Accessibility:** Improve accessibility features for users with disabilities
- **Multilingual Support:** Add support for multiple languages

---

## 🚀 Get Started Today!

Ready to explore Tunisia's hidden gems? Clone the repository, set up your environment, and dive into the code:

```bash
git clone https://github.com/kerfaiyass54/spatial-computing-project.git
cd spatial-computing-project
python webapp.py
```

Visit `http://localhost:5000` to start your journey!

**Star this repository** to show your support and stay updated with the latest developments! 🌟
```

This README.md is designed to be engaging, informative, and actionable. It follows modern GitHub README best practices by:

1. **Including visual elements** like emojis and badges for better readability
2. **Providing clear, step-by-step instructions** for installation and usage
3. **Showing practical code examples** that developers can immediately use
4. **Highlighting key features** with emojis for visual appeal
5. **Encouraging contributions** with clear guidelines
6. **Including a roadmap** to show future development plans
7. **Using modern markdown** features for better organization
8. **Focusing on developer experience** with clear structure and helpful hints

The README also addresses the repository's current state by:
- Explaining the data collection process (2017-2019 timeframe)
- Highlighting the AI components that generate travel guides
- Showing how to extend the project with new data sources
- Providing clear instructions for setting up the development environment

This should help attract contributors and users to the project, leading to more stars and engagement on GitHub.
