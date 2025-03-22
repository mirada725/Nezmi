from Scripts.config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE
from langchain_groq import ChatGroq

class AskAIAgent:
    def __init__(self):
        self.llm = ChatGroq(
            model_name=MODEL_NAME,
            temperature=TEMPERATURE,
            groq_api_key=GROQ_API_KEY
        )

    def ask_ai(self, state):
        """Process a query and return an AI-generated answer"""
        question = state["query"]
        response = self.llm.invoke([{"role": "user", "content": question}])
        return {"answer": response.content}

# ✅ Test your AI agent
if __name__ == "__main__":
    agent = AskAIAgent()
    query = {"query": "What is artificial intelligence?"}
    print(agent.ask_ai(query))  # Expected: AI-generated response
