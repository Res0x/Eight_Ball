from random import choice, randint
def is_correct(txt):
    if txt == 'да' or txt == 'нет':
        return True
    return False
def eight_ball():
    positive = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом']
    neutral_pos = ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да']
    neutral = ['Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять']
    negative = ['Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
    variants = [positive, neutral_pos, neutral, negative]
    print(choice(variants[randint(1,3)]))
def repeat():
    print('Хочешь что-то спросить?')
    answ = input().lower()
    is_correct(answ)
    return answ
def question(na):
    print(f'Задай вопрос могучему шару, {na}:', end=' ')
    questsion = input()
    eight_ball()
def start():
    print('Как тебя зовут, смертный?')
    name = input()
    ans = repeat()
    while ans == 'да':
        question(name)
        ans = repeat()
    print('Возвращайся если возникнут вопросы!')

start()