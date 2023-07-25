import telebot
import math
from telebot import types

token=''
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text='Здравствуйте, здесь вы можете рассчитать стоимость покупки по нынешнему курсу в 元 (китайский юань) '
    keyboard=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=False)
    button1=telebot.types.KeyboardButton('рассчитать стоимость в рублях')
    button2=telebot.types.KeyboardButton('FAQ')
    keyboard.add(button1,button2)
    bot.send_message(message.chat.id,welcome_text,reply_markup=keyboard)
def calculation(message):
    gaid=open('gaid.jpg','rb')
    bot.send_photo(message.chat.id,gaid)
    r=bot.send_message(message.chat.id,'Напишите сумму заказа в юанях') 
    bot.register_next_step_handler(r,answer)
   
def answer(message):
    try:
     course=float(12.9)
     buy=float((message.text).replace(',',''))
     count=math.floor(buy*course+1000)+1800
     bot.send_message(message.chat.id,f'от {count} ₽ - стоимость вашего заказа (с учетом комиссий)')
    except ValueError:
       bot.send_message(message.chat.id,'Не нажимайте слишком часто!')
def curse(message):
   bot.send_message(message.chat.id,'Текущий курс юаня 12.9')
def dost(message):
    bot.send_message(message.chat.id,'Обычно сроки доставки составляют от 16 до 40 дней')
def buy(message):
    bot.send_message(message.chat.id,'Для оформления заказа и уточнения деталей вы можете обратиться сюда:  @wn_market')
   






@bot.message_handler(content_types=['text'])  
def user(message):
    if message.text=='рассчитать стоимость в рублях':
       calculation(message)
    elif message.text=='FAQ':
       keyboard2=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=False)
       button3=telebot.types.KeyboardButton('Какой текущий курс юаня?')
       button4=telebot.types.KeyboardButton('Каковы сроки доставки?')
       button5=telebot.types.KeyboardButton('К кому обратиться для оформления заказа?')
       button6=telebot.types.KeyboardButton('Вернуться в главное меню')
       keyboard2.add(button3,button4,button5,button6)
       bot.send_message(message.chat.id,'Здесь вы можете узнать ответы на часто задаваемые вопросы:',reply_markup=keyboard2)
    elif message.text=='Какой текущий курс юаня?':
       curse(message)
    elif message.text=='Каковы сроки доставки?':
       dost(message)
    elif message.text=='К кому обратиться для оформления заказа?':
       buy(message)
    elif message.text=='Вернуться в главное меню':
       send_welcome(message)
       


bot.polling(non_stop=True,interval=0)



