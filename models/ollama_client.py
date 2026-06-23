import ollama

class OllamaClient:

    def __init__(self, model="qwen3:4b"):
        self.model = model

    def ask(self, prompt):

        response = ollama.chat(
        model=self.model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json",
        options={
            "temperature": 0
        }
        )

        return response["message"]["content"]