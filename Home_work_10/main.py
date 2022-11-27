import telebot, time, math
from telebot import types
from mod_polynom import mn_summ
from mod_log import print_LOG

BOT_TOKEN = '' # Токен Телеграм-бота
bot = telebot.TeleBot(BOT_TOKEN)

TIMEOUT_CONNECTION = 5 # Таймаут переподключения

# Сообщение при старте
START_MESSAGE = """Введите через точку с запятой два многочлена, а я скажу их сумму.

Вот пример:

17x^2 + 2x + 72 = 0 ; 100x^3 + 63x^2 + 58x + 94 = 0

Ответ будет: 100x^3 + 80x^2 + 60x + 166 = 0"""

# Обработчик сообщений-команд
@bot.message_handler(commands=['start'])
def send_start(message):
    print_LOG('%s (%s): %s' %(message.chat.first_name, message.chat.username, message.text))
    print('%s (%s): %s' %(message.chat.first_name, message.chat.username, message.text))
    msg = None

    if message.text.lower() == '/start':
        msg = bot.send_message(message.chat.id, START_MESSAGE, parse_mode='markdown')

    if (msg):
        print('Бот: %s'%msg.text)

# Обработчик всех сообщений
@bot.message_handler(func = lambda message: True)
def answer_to_user(message):
    print_LOG('%s (%s): %s' %(message.chat.first_name, message.chat.username, message.text))
    print('%s (%s): %s' %(message.chat.first_name, message.chat.username, message.text))
    msg = None

    user_message = message.text.lower()
    user_message = user_message.lstrip()
    user_message = user_message.rstrip()
    
    print(user_message)

    if user_message == 'привет':
        msg = bot.send_message(message.chat.id, '*Привет, %s*'%(message.chat.first_name), parse_mode='markdown')

    else:
        try:
            usr_msg = user_message.replace(' ', '')
            if ";" in usr_msg:
                mn1, mn2 = usr_msg.split(';', 1)
                answer = str(mn_summ(mn1, mn2))
                msg = bot.send_message(message.chat.id, 'Сумма многочленов: ' + answer)
            else:
                msg = bot.send_message(message.chat.id, 'Ошибка ввода')
                
        except SyntaxError:
            msg = bot.send_message(message.chat.id, 'Похоже, что вы написали что-то не так. \nИсравьте ошибку и повторите снова')
        except NameError:
            msg = bot.send_message(message.chat.id, 'Переменную которую вы спрашиваете я не знаю. \nИсравьте ошибку и повторите снова')
        except TypeError:
            msg = bot.send_message(message.chat.id, 'Мне кажется, что в выражении присутствует ошибка типов. \nИсравьте ошибку и повторите снова')
        except ZeroDivisionError:
            msg = bot.send_message(message.chat.id, 'В выражении вы делите на ноль. \nИсравьте ошибку и повторите снова')

    if (msg):
        print('Бот: %s'%msg.text)

# Обработчик inline-запроса
@bot.inline_handler(func=lambda query: True)
def inline_answer_to_user(inline_query):
    answer = 0
    answer_list = []
    try:
        answer = str(eval(inline_query.query.lower().replace(' ', '')))
        answer_to_send = answer.replace('*', '\*')
        query_to_send = inline_query.query.replace('*', '\*').lower().replace(' ', '')

        answer_list.append(types.InlineQueryResultArticle(
            id = 0,
            title = 'Отправить с выражением',
            description='%s = %s' % (inline_query.query, answer),
            input_message_content = types.InputTextMessageContent(
                message_text = '%s = *%s*' % (query_to_send, answer_to_send),
                parse_mode = 'markdown'),
        ))

        answer_list.append(types.InlineQueryResultArticle(
            id = 1,
            title = 'Отправить без выражения',
            description='%s' % (answer),
            input_message_content = types.InputTextMessageContent(
                message_text = '*%s*' % (answer_to_send),
                parse_mode = 'markdown'),
        ))
            
    except SyntaxError: answer = False
    except NameError: answer = False
    except TypeError: answer = False
    except ZeroDivisionError: answer = False

    if (not answer):    
        answer_list = []
        answer_list.append(types.InlineQueryResultArticle(
            id = 0,
            title = 'Калькулятор',
            description='Чтобы посичтать выражение - введите его.\nЕсли вы хотите просмотреть справку, то перейдите в диалог со мной и напишите \"/help\"',
            input_message_content = types.InputTextMessageContent(message_text = 'Я хотел посчитать выражение, но нажал не туда')
        ))
    
    bot.answer_inline_query(inline_query.id, answer_list)

# Вход в программу
if (__name__ == '__main__'):
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print ('Ошибка подключения. Попытка подключения через %s сек.'%TIMEOUT_CONNECTION)
            time.sleep(TIMEOUT_CONNECTION)