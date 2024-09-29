from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel, GPT2LMHeadModel, GPT2Tokenizer


# Replace these values with your Flickr API key and secret
FLICKR_API_KEY = "your_flickr_api_key"
FLICKR_API_SECRET = "your_flickr_api_secret"

# Replace "your_geospatial_data" with your actual geospatial data points
geospatial_data_points = [
    {"name": "Location1", "latitude": 33.8869, "longitude": 9.5375},
]

# Initialize CLIP model and processor
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")

# Initialize GPT-2 model and tokenizer
gpt2_model = GPT2LMHeadModel.from_pretrained("gpt2")
gpt2_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def generate_travel_guide(location_data):
    # Replace this with your logic to retrieve an image URL or path for each location
    # For example, you might have a database or API that provides image URLs based on location information.
    # Here, we're using a placeholder URL.
    photo_url = "https://example.com/placeholder_image.jpg"

    # Download the image
    image_path = f"{location_data['name']}_image.jpg"
    image_data = requests.get(photo_url).content
    with open(image_path, "wb") as f:
        f.write(image_data)

    # Load and preprocess the image
    image = Image.open(image_path)
    inputs = clip_processor(text=["a photo"], images=image, return_tensors="pt")

    # Use CLIP model to get image features
    image_features = clip_model(**inputs).last_hidden_state

    # Convert image features to text using GPT-2 model
    image_description_prompt = f"A photo from {location_data['name']}:"
    input_ids = gpt2_tokenizer.encode(image_description_prompt, return_tensors="pt")
    #input_ids = input_ids.to("cuda" if torch.cuda.is_available() else "cpu")
    
    # Generate text description using GPT-2
    output = gpt2_model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2)
    generated_text = gpt2_tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text

if __name__ == "__main__":
    for location_data in geospatial_data_points:
        travel_guide = generate_travel_guide(location_data)
        print(f"Travel Guide for {location_data['name']}:\n{travel_guide}\n")