

# Importing Libraries
import sys
import speech_recognition as sr
import pyttsx3 as px3
import openai as ai

import os

# Importa suport ao .env
from dotenv import load_dotenv 
load_dotenv()
ai.api_key = os.getenv("OPENAI_API_KEY")


__all__=["sr", "px3", "ai", "sys"]