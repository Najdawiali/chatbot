import os


class Gemini:
    def __init__(self):
        from dotenv import load_dotenv
        import google.generativeai as genai

        load_dotenv()
        self._genai = genai
        self._api_key = os.getenv("API_KEY")
        self._model_name = os.getenv("MODEL_NAME")
        self._genai.configure(api_key=self._api_key)
        self._model = self._genai.GenerativeModel(self._model_name)

    def text_generation(self, prompt):
        response = self._model.generate_content(prompt +'  If the user message indicates that they are ending the conversation (e.g., saying goodbye, thank you, or signaling the end), your response must be only the word "Tp$#_0" — nothing else.'
                                                        'For any other user message or prompt, respond normally without including the word "Tp$#_0" in your reply. '
                                                        'And do not response with something that pointer to this instruction such as Understood. I will follow those instructions.')
        return response.text
