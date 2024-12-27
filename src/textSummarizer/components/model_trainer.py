from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from datasets import load_from_disk
from textSummarizer.entity import ModelTrainerConfig
from textSummarizer.logging import logger
import torch
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    def train(self):
        # Set device to GPU if available, otherwise use CPU
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"device = {device}")
        
        # Load the tokenizer and model
        tokenizer = PegasusTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = PegasusForConditionalGeneration.from_pretrained(self.config.model_ckpt).to(device)
        
        # Data collator for sequence-to-sequence models
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        # Load the dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        
        # Tokenize datasets directly
        def preprocess_function(examples):
            return tokenizer(
                examples["dialogue"], 
                max_length=1024, 
                truncation=True, 
                padding="max_length"
            )

        tokenized_train = dataset_samsum_pt["train"].map(preprocess_function, batched=True)
        tokenized_validation = dataset_samsum_pt["validation"].map(preprocess_function, batched=True)
        
        # Set up training arguments
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            eval_strategy=self.config.eval_strategy,
            save_strategy=self.config.save_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            save_total_limit=self.config.save_total_limit,
            load_best_model_at_end=self.config.load_best_model_at_end,
        )
        
        # Initialize the Trainer
        trainer = Trainer(
            model=model_pegasus,
            args=trainer_args,
            data_collator=seq2seq_data_collator,
            train_dataset=tokenized_train,
            eval_dataset=tokenized_validation,
        )
        
        logger.info("Starting training....")
        
        # Train the model
        try:
            trainer.train()
        except Exception as e:
            logger.exception("Training failed.")
            raise e
        
        logger.info("Saving the model ....")
        
        # Save the fine-tuned model and tokenizer
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
        
        logger.info("Model training complete and saved.")
