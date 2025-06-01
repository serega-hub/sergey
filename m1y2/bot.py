
import requests
import telebot
import os
import random
from config import token    
from logic import classify_dog, gen_pass

smiles = ['😎','😀','👍']
money = ['Орел', 'Решка']
rock_scissors_paper = ['ножницы','бумага','камень']
images = ['mem1.jpeg' * 10 ,'mem2.jpeg' * 15,'mem3.jpeg' * 20, 'mem4.jpg']
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! <b>Я твой Telegram бот.</b>\n<blockquote><u>Вот что я умею:</u> \n/hello - <i>приветствие</i> \n/bye - <i>прощание</i> \n/pass - <i>генерирует рандомный пароль</i> \n/random_smile - <i>выводит рандомный смайлик</i> \n/heads_or_tails - <i>Орел или решка?</i> \n/help - <i>поможет вам</i> \n/info - <i>расскажет о боте</i> \n/rock_scissors_paper_game - <i>камень - ножницы - бумага</i> \n/mem - <i>рандомный мем</i> \n/duck - <i>картинка или гиф с уткой</i> \n/nature_new_knowledge - <i>факты про природу</i> </blockquote>", parse_mode='HTML')
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

@bot.message_handler(commands=['nature_new_knowledge'])
def send_nature(message):
    bot.reply_to(message, "Про что вы хотелибы узнать? \n/recycling - <i>переработка</i> \n/decomposition - <i>разложение</i>",parse_mode='HTML')
    
@bot.message_handler(commands=['recycling'])
def send_recycling(message):
    bot.reply_to(message, "Переработка очень важна для нашего мира. \n<blockquote><u>Почему?</u> \nПотому что переработка может предотвратить захоронение потенциально полезных материалов и сократить потребление первичного сырья, тем самым снизив потребление энергии, загрязнение воздуха (от сжигания), загрязнение воды, загрязнение почвы (от захоронения).</blockquote> \n<u>Интересные факты про переработку:</u> \n1 - <i>Переработка 1 тонны стекла экономит 600 кг песка</i> \n2 - <i>Каждая тонна переработанной бумаги, картона и гофрокартона сохраняет 17 деревьев и 26500 литров воды, а также уменьшает загрязнение на 95%, благодаря экономии примерно 1750 литров нефти (11 баррелей).</i> \n3 - <i>Переработка одной алюминиевой банки сохраняет энергию, равную 0,2 литра бензина.</i>",parse_mode='HTML')

@bot.message_handler(commands=['decomposition'])
def send_nature(message):
    bot.reply_to(message, "Разложение это : <i>разрушение, распад сложного объекта на составляющие.</i> \n<u>Время разложение некоторых предметов:</u> \n<b>Виды</b>                                    <b>Период разложение</b> \nПищевые отходы            до 1 месяца \nГазетная бумага              до 1 года \nБумага                                 2 года \nКартонные коробки      до 1 года \nЖелезные банки              до 10 лет \nАвтоаккумуляторы        до 100 лет \nАлюминиевые банки    500 лет \nСтекло                                  более 1000 лет",parse_mode='HTML')


@bot.message_handler(commands=['rock_scissors_paper_game'])
def send_rsp(message):
    bot.reply_to(message, "<u>Выберете:</u> \n/rock - <i>Камень</i> \n/scissors - <i>Ножницы</i> \n/paper - <i>Бумага</i>",parse_mode='HTML')
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

@bot.message_handler(commands=['mem'])
def send_mem(message):
    images = os.listdir('m1y2/images')
    img_name = random.choice(images)
    with open(f'm1y2/images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)



def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
    
    
@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(content_types=['photo'])    
def fotografiya(message):

    if not message.photo:
        return bot.send_message(message.chat.id,'Вы забыли загрузить картинку :(')

    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file) 

    dog = classify_dog(message)
    if dog == 'Вест-хайленд-уайт-терьер Собачка':
        bot.reply_to(message, 'Если вам не нравится то что собаки линяют то эта собака вам подойдёт. Эти собаки не линяют.')
    elif dog == 'Пудель':
        bot.reply_to(message, 'Если вам не нравится то что собаки линяют то эта собака вам подойдёт. Эти собаки не линяют.')
    elif dog == 'Борзая гончая':
        bot.reply_to(message, 'Если вам не нравится то что собаки линяют то эта собака вам подойдёт. Эти собаки не линяют.')
    elif dog == 'Боксер':
        bot.reply_to(message, 'Если вам не нравится то что собаки линяют то эта собака вам подойдёт. Эти собаки не линяют.')
    elif dog == 'Йоркширский терьер':
        bot.reply_to(message, 'Если вам не нравится то что собаки линяют то эта собака вам подойдёт. Эти собаки не линяют.')
    elif dog == 'Мальтийская болонка':
        bot.reply_to(message, 'Если вам не нравится то что собаки линяют то эта собака вам подойдёт. Эти собаки не линяют.')    
    elif dog == 'Эрдельтерьер':
        bot.reply_to(message, 'Если вам не нравится то что собаки линяют то эта собака вам подойдёт. Эти собаки не линяют.')
    elif dog == 'Другие':                        
        bot.reply_to(message, 'Если вам не нравится то что собаки линяют то эта собака вам не подойдёт. Эти собаки линяют.')
        


bot.polling()