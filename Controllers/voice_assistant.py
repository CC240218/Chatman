from  Models.speech_recognition  import  SpeechRecognizer
from  Models.text_to_speech      import  TextToSpeech
from  Models.ai_processor        import  AIProcessor



# 🔹 CONTROLADOR: Orquestra as ações do assistente
class VoiceAssistant:
    """Gerencia a interação entre os componentes do assistente."""
    
    def __init__(self):
        self.speech_recognizer = SpeechRecognizer()
        self.text_to_speech = TextToSpeech()
        self.ai_processor = AIProcessor()

    def run(self):
        """Loop principal do assistente."""
        while True:
            command = self.speech_recognizer.recognize()
            response = self.ai_processor.process(command)
            print("IA:", response)
            self.text_to_speech.speak(response)