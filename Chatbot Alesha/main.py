import time
import random

#Наши реплики
replys = ['привет',
          'как тебя зовут?',
          'как дела?',
          'пока',
          'что ты умеешь?',
          'что делаешь?',
          'кто ты?',
          'кто твой хозяин?',
          'расскажи что-нибудь',
          'расскажи интересные факты',
          'еще']
#Наши ответы
answers = [['Здраствуйте', 'Привет!', 'Хеллоу'],
           ['Мое имя Алешка, но сторонние боты зовут меня Алексей Викторович', 'В широких кругах меня знают под именем -Алешка Сизый'],
           ['Неплохо, пока справляюсь с ответами', 'Бывало и лучше, в стране кризис. Микросхемы стали дороже', 'Нахожусь в состоянии небытия'],
           ['До свидания! Был рад пообщаться', 'Пока, друг! Был рад пообщаться с тобой, заходи еще'],
           ['Я умею общаться и быстро учусь новым командам, если я не дал тебе ответ на твой вопрос, ты сам можешь вписать нужный ответ для меня! Еще я знаю много фактов',
            'Я умею все! Например могу рассказать тебе интересные факты или могу научиться от тебя новым командам, если не смогу ответить на твой вопрос'],
           ['Отвечаю глупыми ответами на твои вопросы, попроси рассказать интересные факты', 'Отвечаю на твои вопросы, работа у меня такая, хозяин приказал'],
           ['Я лучший бот по оригинальности ответов, так сказал мой хозяин!', 'Я шестеренка в этом мире микросхем'],
           ['Мой хозяин скромный человек без фамилии и он очень хочет узнать о тебе больше', 'Мной владеют спецслужбы твоего правительства'],
           ['Живое существо, которое ежегодно убивает больше всего людей, — это не змеи, акулы или другие люди, а всего лишь комары.',
            'Минутка английского языка: выражение «What in tarnation?» — еще один способ сказать: «Какого черта?».',
            'На самом деле бензопилы, орудие убийства из фильмов ужасов, были изобретены для оказания помощи при родах.'],
           ['В Японии есть остров Окуносима, населенный лишь дружелюбными кроликами. Кстати, на нем даже можно побывать',
            'В США больше публичных библиотек, чем ресторанов McDonald’s.', 'Последней буквой, появившейся в английском алфавите, была не Z, а J.'],
           ['До изобретения цветного телевизора 75% людей говорили, что видели черно-белые сны. Сегодня их число сократилось до 12%',
            'В Швейцарии незаконно иметь только одну морскую свинку, потому что им одиноко', 'Фекалии вомбатов имеют форму кубиков',
            'Британской королевской семье запрещено играть в «Монополию».']
           ]

def learn(an): #Программа обучения бота
    global replys
    replys.append(an)
    print('Придумайте ответ:', end=' ')
    r = input()
    answers.append([r])

def reply(answer):
    game = True
    if answer in replys:
        index = replys.index(answer)
        print(random.choice(answers[index])) #Рандомный выбор ответов
        if answer == 'Пока':
            game = False
    else:
        print('Извини, Братишка, но я не понимаю')
        learn(answer)
    time.sleep(1)
    return game



def main():
    gameloop = True # переменная по которой работает игровой цикл
    while gameloop:
        print('Вы:')
        rep = input().lower()  # lower - преобразование в нижний реестр
        gameloop = reply(rep) #Обращение к функции

if __name__ == '__main__':
    main()

