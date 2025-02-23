from config import sr

# 🔹 MODELO: Captura de voz
class SpeechRecognizer:
    """Captura e converte a fala em texto."""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 300  # Ajuste de sensibilidade
        self.recognizer.pause_threshold = 2  # Tempo antes de processar após uma pausa

    def recognize(self):
        """Escuta e retorna o comando falado."""
        with sr.Microphone() as source:
            print("Diga algo...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=None)  # Aguarda fala completa
        
        try:
            command = self.recognizer.recognize_google(audio, language="pt-BR")
            print("Você disse:", command)
            return command.lower()
        except sr.UnknownValueError:
            return "Não entendi."
        except sr.RequestError:
            return "Erro no serviço de reconhecimento de voz."