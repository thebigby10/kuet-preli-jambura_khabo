from transformers import Seq2SeqTrainer, Seq2SeqTrainingArguments

def train_model(model, tokenizer, train_data, val_data):
    # Define training arguments
    training_args = Seq2SeqTrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        num_train_epochs=3,
        weight_decay=0.01,
        save_total_limit=2,
        predict_with_generate=True,
        fp16=True,  # Enable if using GPU
    )

    # Initialize Trainer
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=train_data,
        eval_dataset=val_data,
        tokenizer=tokenizer,
    )

    # Train the model
    trainer.train()

    # Save the trained model
    trainer.save_model("./banglish_to_bengali_model")
