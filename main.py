from    config import sys
from    Controllers.voice_assistant import VoiceAssistant
import  config

# Suporte para caracteres especiais
sys.stdout.reconfigure(encoding='utf-8')







# 🔹 EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()

