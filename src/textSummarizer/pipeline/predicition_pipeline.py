from src.textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, pipeline
import torch

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        # ✅ use GPU if available
        device = 0 if torch.cuda.is_available() else -1

        pipe = pipeline(
            "summarization",
            model=self.config.model_path,
            tokenizer=tokenizer,
            device=device  # -1 = CPU, 0 = first GPU
        )

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        cleaned_output = output.replace("<n>", "\n").strip()
        return cleaned_output
