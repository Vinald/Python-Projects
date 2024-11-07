from gtts import gTTS
import os

# the text that you want to convert to audio
my_text = 'Samuel is a computer engineer'

# Language in which you want to convert
language = 'en'

# Converting the text to audio
output = gTTS(text=my_text, lang=language, slow=False)
output.save('output.mp3')

# Playing the converted file
os.system('start output.mp3')