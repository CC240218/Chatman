from config import px3


# 🔹 MODELO: Conversão de texto para fala
class TextToSpeech:
    """Converte texto em áudio."""
    
    def __init__(self):
        self.engine = px3.init()

    def speak(self, text):
        """Faz a IA falar."""
        self.engine.say(text)
        self.engine.runAndWait()