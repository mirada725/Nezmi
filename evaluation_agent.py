from googleapiclient.discovery import build
from Scripts.config import YOUTUBE_API_KEY,YOUTUBE_MAX_RESULTS

class EvaluationAgent:
    def __init__(self):
        self.youtube = build("youtube",'v3',developerKey=YOUTUBE_API_KEY)

    def categorize_query(self,query):
        """Categorize the query based on keywords"""
        query_lower=query.lower()
        if any(word in query_lower for word in ["tutorial","how to","learn"]):
            return "educational"
        elif any(word in query_lower for word in ["news","update","latest"]):
            return "news"
        return "general"
    
    def fetch_videos(self,query):
        """Fetch videos from YouTube based on the query"""
        search_response = self.youtube.search().list(
            q=query,
            part="id,snippet",
            maxResults=YOUTUBE_MAX_RESULTS
        ).execute()

        video_links=[]
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                video_links.append(f"https://www.youtube.com/watch?v={search_result['id']['videoId']}")
        return video_links
    
    def evaluate(self,state):
        """Process a query and return"""
        query = state["query"]
        category = self.categorize_query(query)
        video_links=self.fetch_videos(query)
        return {"category": category, "videos": video_links}
    
if __name__ == "__main__":
    agent = EvaluationAgent()
    query = input("Enter your search query: ")  # Get user input
    result = agent.evaluate({"query": query})
    print(result)  # Print the category and video links
      