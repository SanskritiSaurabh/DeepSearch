import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        "tavily_api_key": os.getenv("TAVILY_API_KEY"),
        "google_api_key": os.getenv("GOOGLE_API_KEY")
    }