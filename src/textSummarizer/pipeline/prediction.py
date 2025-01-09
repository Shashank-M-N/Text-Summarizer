from textSummarizer.config.configuration import ConfigurationManager
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        try:
            # Check for empty input
            if text.strip() == "":
                raise ValueError("Input text cannot be empty. Please provide valid text.")

            # Load the tokenizer and model that you trained
            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
            model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)

            # Create the summarization pipeline using your trained model
            pipe = pipeline("summarization", model=model, tokenizer=tokenizer)

            # Set generation arguments
            gen_kwargs = {
                "length_penalty": 0.8,
                "num_beams": 8,
                "max_length": 128
            }

            print("Dialogue:")
            print(text)

            output = pipe(text, **gen_kwargs)
            print(output)  # Print to inspect the full output

            summary = output[0]["summary_text"]
            if not summary:
                print("No summary returned.")
            else:
                print("\nModel Summary:")
                print(summary)
                return summary

        except ValueError as ve:
            print(f"Input Error: {ve}")
            return str(ve)  # Return error message for empty input

        except Exception as e:
            print(f"Error during summarization: {e}")
            return None
