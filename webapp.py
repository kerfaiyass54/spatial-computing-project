from flask import Flask, render_template, url_for, jsonify  # Import jsonify
import os

app = Flask(__name__)

# Dictionary of locations and their descriptions
locations_data = {
    'Tozeur': 'Tozeur, a picturesque oasis town in southwestern Tunisia, is a desert gem that beckons tourists with its unique charm. Nestled on the edge of the expansive Sahara, Tozeur is renowned for its lush palm groves, centuries-old architecture, and traditional earthen dwellings. Visitors can wander through the medina, explore the distinctive brickwork of the old town, and experience the mesmerizing Chak Wak Park. Tozeur serves as a gateway to the mesmerizing landscapes of the Chott el Jerid salt flats and the mystical desert, offering a perfect blend of cultural richness and natural wonders for an unforgettable Tunisian adventure',
    'Carthage': 'Carthage, nestled along the Tunisian coast, is an ancient city of historical significance and archaeological marvels. Founded by Phoenician settlers, it evolved into a powerful Carthaginian empire, rivaling Rome. Today, UNESCO-listed Carthage invites tourists to explore its Punic Ports, Byrsa Hill, Roman Amphitheatre, Antonine Baths, and Tophet. The Cathedral of Saint Louis and Carthage Museum offer glimpses into its diverse history. With panoramic views, ancient ruins, and a rich tapestry of artifacts, Carthage is a captivating destination for those eager to uncover the remnants of an influential Mediterranean civilization.',
    'Gabes': 'Gabes, a coastal city in southeastern Tunisia, invites tourists to explore its dynamic blend of history, culture, and natural beauty. The city is renowned for its vibrant souks, where the lively atmosphere and diverse array of goods showcase the local way of life. History enthusiasts can delve into the archaeological wonders of the region, such as the Roman city of Tacape and the Medenine archaeological museum. With its pristine beaches along the Gulf of Gabes, the city offers a relaxing escape, while the nearby oasis of Gabes offers a glimpse into traditional agriculture with its verdant palm groves. Gabes stands as a gateway to the enchanting landscapes of southern Tunisia, promising visitors an enriching and diverse travel experience.',
    # Add more locations as needed
}

@app.route('/')
def home():
    title = "Tunisian Tourist Destinations"
    description = "Based on pictures taken by tourists, these are the most popular locations visited between 2017 and 2023."
    
    image1_path = url_for('static', filename='points.jpg')
    image2_path = url_for('static', filename='detailed_administrative_map_of_tunisia_with_cities_1.jpg')

    return render_template('index.html', title=title, description=description, image1_path=image1_path, image2_path=image2_path)

@app.route('/get_travel_guides')
def get_travel_guides():
    return jsonify({'travel_guides': locations_data})

@app.route('/generate_travel_guide', methods=['POST'])
def generate_travel_guide_endpoint():
    # You may need to modify the logic here based on your requirements
    # For example, you can pass the location information from the frontend
    location_data = {'name': 'Location1'}  # Placeholder data, update accordingly
    travel_guide = locations_data.get(location_data['name'], 'No description available for this location.')
    return jsonify({'travel_guide': travel_guide})

if __name__ == '__main__':
    app.run(debug=True)
