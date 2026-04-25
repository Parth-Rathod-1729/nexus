import sys
from gtts import gTTS

try:
    tts = gTTS(text="Ab hum dekhte hain ki graph kaise increase ho raha hai", lang='en', tld='co.in')
    tts.save("test_co_in.mp3")
    print("Success with tld='co.in'")
except Exception as e:
    print(f"Error: {e}")
