
from config import ai


# 🔹 MODELO: Processamento da IA
class AIProcessor:
    """Processa o comando de voz com a OpenAI."""
    
   # def __init__(self, api_key):
   #    ai.api_key = api_key

    def process(self, command):
        """Interpreta e responde ao comando do usuário."""
        if "assistente" in command:  # Nome do assistente
            response = ai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": command}]
            )
            return response["choices"][0]["message"]["content"]
        return "Diga meu nome para ativar."