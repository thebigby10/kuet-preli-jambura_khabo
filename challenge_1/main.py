from preprocessing import load_and_preprocess_data
from model import get_model_and_tokenizer
from train import train_model

def main():
    # Load and preprocess data
    train_data, val_data, tokenizer = load_and_preprocess_data()

    # Get model and tokenizer
    model = get_model_and_tokenizer()

    # Train the model
    train_model(model, tokenizer, train_data, val_data)

if __name__ == "__main__":
    main()
