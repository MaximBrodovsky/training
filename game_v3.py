import numpy as np

def predict_number(number: int, number_range: tuple, count: int) -> int:
    """Guess number with binary search 

    Args:
        number (int): Number we need to guess
        number_range (tuple): Range for the number
        count (int): Count of previous attempts

    Returns:
        int: Count of attempts
    """
    if number > (number_range[0] + (number_range[1] - number_range[0])//2):
        return predict_number(number, (number_range[0] + (number_range[1] - number_range[0])//2 + 1, number_range[1]), count + 1)
    elif number < (number_range[0] + (number_range[1] - number_range[0])//2):
        return predict_number(number, (number_range[0], number_range[0] + (number_range[1] - number_range[0])//2 - 1), count + 1)
    else:
        return count + 1

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(predict_number(number, (1, 100), 0))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(random_predict)

#print(predict_number(1, (1, 100), 0))
#print(predict_number(100, (1, 100), 0))
#print(predict_number(50, (1, 100), 0))
#print(predict_number(86, (1, 100), 0))