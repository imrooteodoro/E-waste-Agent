import google.generativeai as genai
from auth.auth import authenticate


class BotService:

    @staticmethod
    def connect_agent(system_context:str, user_message:str) -> str:
        genai.configure(api_key = authenticate())
        generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 20,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
        system_instruction=f"{system_context}",
        )

        chat_session = model.start_chat(
        history=[
        ]
        )

        response = chat_session.send_message(f"{user_message}")

        return response.text
