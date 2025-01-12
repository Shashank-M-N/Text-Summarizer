from textSummarizer.config.configuration import ConfigurationManager
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

def chunk_text(text, tokenizer, max_tokens):
    """
    Chunk a long text into smaller pieces based on the tokenizer's maximum token limit.

    Args:
        text (str): The input text to be chunked.
        tokenizer (transformers.PreTrainedTokenizer): The tokenizer used for the model.
        max_tokens (int): The maximum number of tokens the model can process.

    Returns:
        List[str]: A list of text chunks.
    """
    # Tokenize the input text
    tokens = tokenizer.encode(text, truncation=False)
    
    # Split tokens into chunks of size `max_tokens`
    chunks = [tokens[i:i + max_tokens] for i in range(0, len(tokens), max_tokens)]
    
    # Decode tokens back to text
    text_chunks = [
        tokenizer.decode(chunk, skip_special_tokens=True, clean_up_tokenization_spaces=True) 
        for chunk in chunks
    ]
    
    return text_chunks

class PredictionPipeline:
    def __init__(self):
        # Load your configuration (update paths as needed)
        self.config = ConfigurationManager().get_model_evaluation_config()
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)
        self.pipe = pipeline("summarization", model=self.model, tokenizer=self.tokenizer)

    def predict(self, text):
        try:
            # Check for empty input
            if text.strip() == "":
                raise ValueError("Input text cannot be empty. Please provide valid text.")

            # Maximum token limit for the model
            max_tokens = self.tokenizer.model_max_length - 10
            
            # Chunk the input text
            text_chunks = chunk_text(text, self.tokenizer, max_tokens)
            
            print(f"Input text has been divided into {len(text_chunks)} chunks.")

            # Process each chunk through the summarization pipeline
            summaries = []
            for i, chunk in enumerate(text_chunks):
                print(f"\nProcessing Chunk {i + 1}/{len(text_chunks)}:\n{chunk}\n")
                summary = self.pipe(chunk, max_length=128, num_beams=8, length_penalty=0.8)[0]["summary_text"]
                summaries.append(summary)
            
            # Combine all the summaries
            final_summary = " ".join(summaries)
            
            return final_summary

        except ValueError as ve:
            print(f"Input Error: {ve}")
            return str(ve)  # Return error message for empty input

        except Exception as e:
            print(f"Error during summarization: {e}")
            return None
