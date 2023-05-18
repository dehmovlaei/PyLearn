import random
import qrcode
import telebot
from telebot import types
import khayyam
import gtts

main_keyboard = types.ReplyKeyboardMarkup(row_width=3)
key1 = types.KeyboardButton('/start',)
key2 = types.KeyboardButton('/game')
key3 = types.KeyboardButton('/age')
key4 = types.KeyboardButton('/voice')
key5 = types.KeyboardButton('/max')
key6 = types.KeyboardButton('/argmax')
key7 = types.KeyboardButton('/qrcode')
key8 = types.KeyboardButton('/help')
key9 = types.KeyboardButton('/fal')
main_keyboard.add(key1, key2, key3, key4, key5, key6, key7, key8, key9)

game_keyboard = types.ReplyKeyboardMarkup(row_width=2)
key10 = types.KeyboardButton('/NewGame')
key11 = types.KeyboardButton('/Exit')
game_keyboard.add(key10, key11)

back_keyboard = types.ReplyKeyboardMarkup(row_width=1)
key12 = types.KeyboardButton('/Back')
back_keyboard.add(key12)

bot = telebot.TeleBot('TOKEN', parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'HELLO ' + message.from_user.first_name + ' ' + message.from_user.last_name + '\nfor more info use /help command', reply_markup=main_keyboard)

@bot.message_handler(commands=['game'])
def game(message):
    bot.send_message(message.chat.id, 'guess an number between 1 and 50', reply_markup=game_keyboard)
    global position
    global rand_number
    rand_number = random.randint(1, 50)
    position = 1

@bot.message_handler(commands=['age'])
def calc_age(message):
    bot.send_message(message.chat.id, 'enter your jalali birth day in this format: YYYY/MM/DD', reply_markup=back_keyboard)
    global position
    position = 2
    
@bot.message_handler(commands=['voice'])
def text_voice(message):
    bot.send_message(message.chat.id, 'enter an english string:',reply_markup=back_keyboard)
    global position
    position = 3

@bot.message_handler(commands=['max'])
def max(message):
    bot.send_message(message.chat.id, 'enter list with this format: 1,2,3...', reply_markup=back_keyboard)
    global position
    position = 4
    
@bot.message_handler(commands=['argmax'])
def max_arg(message):
    bot.send_message(message.chat.id, 'enter list with this format: 1,2,3...', reply_markup=back_keyboard)
    global position
    position = 5
    
@bot.message_handler(commands=['qrcode'])
def make_qrcode(message):
    bot.send_message(message.chat.id, 'input a string for generate QR:', reply_markup=back_keyboard)
    global position
    position = 6

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.chat.id, '/start: StartBot \n/game: Play guess number\n/age: calculate your age\n'
		  '/voice: convert en string  to voice\n/max: find max element in list\n /argmax: return index of max element in list\n'
		  '/qrcode: generate QR code from a string\n/help show help menu \n/fal some funny sentences')
	
@bot.message_handler(commands=['fal'])
def send_fal(message):
	falList = ['به فنا خواهی رفت', 'به دیدار یار خواهی رفت', 'به سفر خواهی رفت', 'از خود برون شو', 'اندکی صبر سحر نزدیک است']
	selectFal = random.choice(falList)
	bot.send_message(message.chat.id, selectFal)

@bot.message_handler(commands=['NewGame'])
def new_game(message):
    bot.send_message(message.chat.id, 'guess an number between 1 and 50', reply_markup=game_keyboard)
    global position
    global rand_number
    rand_number = random.randint(1, 50)
    position = 1
    
@bot.message_handler(commands=['Exit'])
def exit(message):
	global position
	position = 0
	bot.send_message(message.chat.id, 'select a command:', reply_markup=main_keyboard)

@bot.message_handler(commands=['Back'])
def back(message):
	global position
	position = 0
	bot.send_message(message.chat.id, 'select a command:', reply_markup=main_keyboard)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	global position
	global rand_number
	user_input = message.text
	if position == 1:
		user_number = int(message.text)
		if user_number > 0:
			while True:
				if user_number == rand_number:
					result = " YOU WIN "
					bot.send_message(message.chat.id, result, reply_markup=game_keyboard)
					position = 0
					break
				elif user_number < rand_number:
					result = "GO UP"
					bot.send_message(message.chat.id, result, reply_markup=game_keyboard)
					break
				elif user_number > rand_number:
					result = "GO DOWN"
					bot.send_message(message.chat.id, result, reply_markup=game_keyboard)
					break
	elif position == 2:
		date_of_birth = (str(message.text)).split("/")
		difference = khayyam.JalaliDatetime.now() - khayyam.JalaliDatetime(date_of_birth[0], date_of_birth[1], date_of_birth[2])
		year = difference.days // 365
		kabiseh = year // 4
		difference = (difference.days % 365) - kabiseh
		month = difference // 30
		day = difference % 30
		bot.send_message(message.chat.id, "Your exact age is: "+ str(year) + " years and "+ str(month) + " months and "+ str(day) + " days.")
	elif position == 3:
		en_voice = gtts.gTTS(message.text, lang='en')
		en_voice.save('en.mp3')
		voice = open('en.mp3', 'rb')
		bot.send_voice(message.chat.id, voice)
	elif position == 4:
		max_num = 0
		input_list = str(message.text).split(',')
		for num in input_list:
			if int(num) > max_num:
				max_num = int(num)
		bot.send_message(message.chat.id, 'maximum number: ' + str(max_num))
	elif position == 5:
		max_num = 0
		input_list = str(message.text).split(',')
		for id, num in enumerate(input_list):
			if int(num) > max_num:
				max_num = int(num)
				max_index = id
		bot.send_message(message.chat.id, 'maximum number index: ' + str(max_index))
	elif position == 6:
		user_qrcode = qrcode.make(message.text)
		user_qrcode.save("QR.jpg")
		QR_file = open("QR.jpg", "rb")
		bot.send_photo(message.chat.id, QR_file)
	elif message.text == 'سلام':
		bot.reply_to(message, '👋علیک سلام')
	elif message.text == 'خوبی':
		bot.reply_to(message, '🙏سپاسگزارم')
	elif message.text == 'دوستت دارم':
		bot.reply_to(message, '❤️')
	elif message.text == 'عکس قدی بده':
		photo = open('/Juan Moreno y Herrera–Jiménez.jpeg', 'rb')
		bot.send_photo(message.chat.id, photo)
	elif message.text == 'fal':
		send_fal(message)
	else:
		bot.reply_to(message, 'i can not understand what you say...🙄', reply_markup = main_keyboard)
		
bot.infinity_polling()
