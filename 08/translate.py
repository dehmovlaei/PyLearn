def readFromFile():
    global wordsBank
    f =  open('08/translate.txt', 'r')
    tmp = f.read().split('\n')
    wordsBank = []

    for i in range(0, len(tmp), 2):
        myDic = {'en': tmp[i], 'fa': tmp[i+1]}
        wordsBank.append(myDic)
    f.close
    
def translateEn2Fa():
    userText = input('enter your english text: ')
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
    ...

def add():
     ...

def showMenu():
    print('welcome to my translator')
    print('1- translate english to persian')
    print('2- translate persian to english ')
    print('3- add new word to data base')
    print('4- exit')
  
readFromFile()
showMenu()
choice = int(input('enter your choice: '))
if choice == 1:
    translateEn2Fa()
elif choice == 2:
    translateFa2En()
elif choice == 3:
    add()
elif choice == 4:
    exit(0)