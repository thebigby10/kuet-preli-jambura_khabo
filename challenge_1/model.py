from transformers import AutoModelForSeq2SeqLM

def get_model_and_tokenizer():
    # Load pre-trained model
    model = AutoModelForSeq2SeqLM.from_pretrained("google/mt5-small")
    return model
