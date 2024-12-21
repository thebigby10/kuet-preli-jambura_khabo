from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("google/mt5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/mt5-small")

# Function to translate Banglish to Bengali
def translate_banglish_to_bengali(banglish_text):
    # Tokenize input text
    inputs = tokenizer(banglish_text, return_tensors="pt", padding=True, truncation=True)

    # Generate translation
    with torch.no_grad():
        translated_tokens = model.generate(**inputs, max_length=128)

    # Decode the translated text
    bengali_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return bengali_text

# Define the API route for transliteration
@app.route('/transliterate', methods=['POST'])
def transliterate():
    # Get Banglish text from POST request
    data = request.get_json()
    banglish_text = data.get("banglish_text", "")

    # Check if text is provided
    if not banglish_text:
        return jsonify({"error": "No Banglish text provided"}), 400

    # Translate to Bengali
    bengali_text = translate_banglish_to_bengali(banglish_text)

    # Return the result in JSON format
    return jsonify({"bengali_text": bengali_text})


if __name__ == "__main__":
    main()
