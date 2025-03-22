from groq import Groq

GROQ_API_KEY = "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"  # Replace with your actual API key

client = Groq(api_key=GROQ_API_KEY)

try:
    models = client.models.list()
    print("Available Models:")
    for model in models.data:
        print(f"- {model.id}")
except Exception as e:
    print("Error fetching models:", e)
