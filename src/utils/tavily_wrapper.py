from tavily import TavilyClient

class TavilySearch:
    def __init__(self, api_key):
        self.client = TavilyClient(api_key=api_key)
    
    def search(self, query, max_results=5):
        response = self.client.search(
            query=query,
            search_depth="advanced",
            max_results=max_results,
            include_answer=True
        )
        return {
            "summary": response.get("answer", ""),
            "sources": response.get("results", [])[:max_results]
        }