import google.generativeai as genai

class Gemini:
    def __init__(self, name:str, generation_config, safety_settings):
        self.name = name
        self.generation_config = generation_config
        self.safety_settings = safety_settings

    def configure_generation(self, generation_config):
        self.generation_config = generation_config
        
    def configure_safety_settings(self, safety_settings):
        self.safety_settings = safety_settings

    def get_safety_settings():
        return [
          {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
          {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
          },
        ]

        self.model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                           generation_config=generation_config,
                                           safety_settings=safety_settings) 