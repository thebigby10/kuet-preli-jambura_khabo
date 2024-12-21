from datasets import load_dataset
from transformers import AutoTokenizer

def load_and_preprocess_data():
    # Load dataset
    dataset = load_dataset("SKNahin/bengali-transliteration-data")
    dataset = dataset["train"].train_test_split(test_size=0.2)

    train_data = dataset["train"]
    val_data = dataset["test"]

    # Tokenizer
    tokenizer = AutoTokenizer.from_pretrained("google/mt5-small")

    # Preprocess function
    def preprocess_function(examples):
        inputs = examples["banglish_text"]
        targets = examples["bengali_text"]
        model_inputs = tokenizer(inputs, text_target=targets, truncation=True, max_length=128)
        return model_inputs

    # Tokenize datasets
    train_data = train_data.map(preprocess_function, batched=True)
    val_data = val_data.map(preprocess_function, batched=True)

    return train_data, val_data, tokenizer
