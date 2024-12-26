import telebot
import random
from config import token    
from logic import gen_pass
smiles = ['😎','😀','👍']
money = ['Орел', 'Решка']
rock_scissors_paper = ['ножницы','бумага','камень']
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(token)
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! <b>Я твой Telegram бот.</b>\n<blockquote><u>Вот что я умею:</u> \n/hello - <i>приветствие</i> \n/bye - <i>прощание</i> \n/pass - <i>генерирует рандомный пароль</i> \n/random_smile - <i>выводит рандомный смайлик</i> \n/heads_or_tails - <i>Орел или решка?</i> \n/help - <i>поможет вам</i> \n/info - <i>расскажет о боте</i> \n/rock_scissors_paper_game - <i>камень - ножницы - бумага</i></blockquote>", parse_mode='HTML')
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока, удачи!")
    
@bot.message_handler(commands=['pass'])
def send_pass(message):
    password = gen_pass(10)
    bot.reply_to(message, f"Ваш пароль: {password}")

@bot.message_handler(commands=['help'])
def send_bye(message):
    bot.reply_to(message, "Этот бот отвечяет на определённые запросы! \n<blockquote>Эти запросы вы можете посмотреть в приветственном сообщении нажав /start</blockquote>", parse_mode='HTML')

@bot.message_handler(commands=['info'])
def send_bye(message):
    bot.reply_to(message, "Это мой первый бот. \n<blockquote><u>Что умеет этот бот?</u> \nЭтот бот умеет отвечать на некоторые запросы. Эти запросы вы можете посмотреть в приветственном сообщении нажав /start</blockquote>", parse_mode='HTML')

@bot.message_handler(commands=['random_smile'])
def send_rs(message):
    x = random.choice(smiles)
    bot.reply_to(message,x)

@bot.message_handler(commands=['heads_or_tails'])
def send_hot(message):
    y = random.choice(money)
    bot.reply_to(message,y)

@bot.message_handler(commands=['rock_scissors_paper_game'])
def send_rsp(message):
    bot.reply_to(message, "Ка-мень \nНож-ни-цы \nБу-ма-га \nРаз \nДва \nТри \n<u>Выберете:</u> \n/rock - <i>Камень</i> \n/scissors - <i>Ножницы</i> \n/paper - <i>Бумага</i>",parse_mode='HTML')
    while True:

        #   Paper
        @bot.message_handler(commands=['paper'])
        def send_onepaper(message):
            z = random.choice(rock_scissors_paper)
            if z == 'ножницы':
                bot.reply_to(message,f'Бот выбрал: {z}')
                bot.reply_to(message,'Сорян, вы проиграли. Бот выиграл!')

            elif  z == 'камень':
                bot.reply_to(message,f'Бот выбрал: {z}')
                bot.reply_to(message,'Ура!!! Вы выиграли!')

            else:
                bot.reply_to(message,f'Бот выбрал: {z}')
                bot.reply_to(message,'Ничья')

        #   Scisssors
        @bot.message_handler(commands=['scissors'])
        def send_onepaper(message):
            z = random.choice(rock_scissors_paper)
            if z == 'камень': 
                bot.reply_to(message,f'Бот выбрал: {z}')        
                bot.reply_to(message,'Упс. Бот выиграл ((')

            elif z == 'бумага':
                bot.reply_to(message,f'Бот выбрал: {z}')
                bot.reply_to(message,'Вы выиграли, супер!')

            else:
                bot.reply_to(message,f'Бот выбрал: {z}')
                bot.reply_to(message,'Ничья...')

            
        #   Rock
        @bot.message_handler(commands=['rock'])
        def send_onepaper(message):
            z = random.choice(rock_scissors_paper)
            if z == 'бумага':
                bot.reply_to(message,f'Бот выбрал: {z}')
                bot.reply_to(message,'Ну, вот... Бот выиграл...')

            elif z == 'ножницы':
                bot.reply_to(message,f'Бот выбрал: {z}')
                bot.reply_to(message,'Отлично! Вы выиграли!')
        
            else:
                bot.reply_to(message,f'Бот выбрал: {z}')
                bot.reply_to(message,'Эх... Ничья!')
#
        
bot.polling()
