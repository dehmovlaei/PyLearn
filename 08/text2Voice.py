import gtts

myText = 'پژگچ '
voice = gtts.gTTS(myText, lang='ar', slow=False)
voice.save('08/voice.mp3')