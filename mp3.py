from gtts import gTTS

data = gTTS('hello there, how are you')

data.save('test.mp3')