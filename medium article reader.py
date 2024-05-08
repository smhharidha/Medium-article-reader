import pyttsx3
import requests
from bs4 import BeautifulSoup
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def main():
    url = input("Paste article URL:\n")
    res = requests.get(url)
    
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        articles = [p.getText().strip() for p in soup.select('p')]
        text = " ".join(articles)
        speak(text)

        # Save output audio to a file
        desktop_path = os.path.expanduser("~/Desktop")
        filename = os.path.join(desktop_path, "output.wav")
        engine.save_to_file(text, filename)
        engine.runAndWait()

        print("Output audio saved successfully.")
    else:
        print("Failed to fetch the content from the URL.")

if __name__ == "__main__":
    main()
