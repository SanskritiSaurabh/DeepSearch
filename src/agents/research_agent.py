import google.generativeai as genai
from utils.tavily_wrapper import TavilySearch
from utils.config import get_config

config = get_config()

class ResearchAgent:
    def __init__(self, config):
        if not config.get("tavily_api_key"):
            raise ValueError("Tavily API key is missing. Add it to your .env file.")
        if not config.get("google_api_key"):
            raise ValueError("Google API key is missing. Add it to your .env file.")
        
        self.tavily = TavilySearch(config["tavily_api_key"])
        genai.configure(api_key=config["google_api_key"])
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest')  # Updated model name
    
    def run(self, query):
        try:
            # Perform web search
            research_data = self.tavily.search(query)
            
            # Summarize research using Gemini
            prompt = f"Summarize this research for a query: {query}\n\nResearch Data: {research_data}"
            response = self.model.generate_content(prompt)
            
            return response.text
        except Exception as e:
            return f"Research error: {str(e)}"