import os
import gtts

def readFromFile():
    global wordsBank
    if os.path.exists('08/translate.txt'):
        f =  open('08/translate.txt', 'r')
        tmp = f.read().split('\n')
        wordsBank = []
        for i in range(0, len(tmp)-1, 2):
            myDic = {'en': tmp[i], 'fa': tmp[i+1]}
            wordsBank.append(myDic)
        f.close
    else:
        print('file not exist:')
        exit(0)

def writeToDataBase():
    f = open('08/translate.txt', 'w')
    for word in wordsBank:
        f.write(word['en'] + '\n' + word['fa'] + '\n')
    f.close
    
def translateEn2Fa():
    userText = str(input('enter your english text: ')).replace('.', '')
    userWords = userText.split(' ')
    output = ''
    for userWord in userWords:
        for word in wordsBank:
            if userWord == word['en']:
                output = output + (word['fa']) + ' '
                break
        else:
            output = output + userWord + ' '
    print(output)

def translateFa2En():
    userText = str(input('enter your finglish text: ')).replace('.', '')
    userWords = userText.split(' ')
    output = ''
    for userWord in userWords:
        for word in wordsBank:
            if userWord == word['fa']:
                output = output + (word['en']) + ' '
                break
        else:
            output = output + userWord + ' '
    print(output)
    voice = gtts.gTTS(output, lang='en', slow=False)
    voice.save('08/enTranslatedVoice.mp3')

def add():
    en = input('enter english word: ')
    fa = input('enter finglish word: ')
    newWord = {'en': en, 'fa': fa}
    wordsBank.append(newWord)

def showMenu():
    print('welcome to my translator')
    print('1- translate english to persian')
    print('2- translate persian to english ')
    print('3- add new word to data base')
    print('4- exit')
  
readFromFile()
while(True):
    showMenu()
    choice = int(input('enter your choice: '))
    if choice == 1:
        translateEn2Fa()
    elif choice == 2:
        translateFa2En()
    elif choice == 3:
        add()
    elif choice == 4:
        print(wordsBank)
        writeToDataBase()
        exit(0)