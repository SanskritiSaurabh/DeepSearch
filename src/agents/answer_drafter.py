import google.generativeai as genai
from utils.config import get_config

config = get_config()

class AnswerDrafter:
    def __init__(self, config):
        if not config.get("google_api_key"):
            raise ValueError("Google API key is missing. Add it to your .env file.")
        
        genai.configure(api_key=config["google_api_key"])
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')  # Updated model name
    
    def run(self, data, query):
        try:
            prompt = f"Draft a concise answer using this data: {data}\n\nOriginal Query: {query}"
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Answer drafting failed: {str(e)}"