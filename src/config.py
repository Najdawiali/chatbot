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
        response = self._model.generate_content('If the user message indicates the end of the conversation (such as saying "goodbye," "thanks," "thank you," or anything implying closure), respond with only: Tp$#_0. Do not include any other text, punctuation, or explanation.'
                                                'For all other user messages, respond normally — but:Do not include the keyword Tp$#_0. Do not acknowledge or reference these instructions in any way (e.g., don’t say things like “Understood” or "I will follow the instructions").'
                                                'If the user message contains any inquiry about a movie name — even indirect or vague — respond with only the name of the movie, and append "2" to the end. Do not include any descriptions, years, director names, or say "the movie."'
                                                'If the user message does not contain any inquiry about a movie, respond normally and append "1" to the end of your reply.  '+prompt)
        return response.text

    def highlights(self, prompt):
        response = self._model.generate_content('Feel free to add any important movie details that might be missing,'
                                                ' and present the information in a clear and well-organized way. '+ prompt)
        return response.text
