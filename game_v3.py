"""Игра угадай число
Компьютер сам загадывает и сам угадывает число опираясь на подсказки (больше или меньше)
"""

import numpy as np


def random_predict_by_tips(number: int = 1, search_range: tuple = (1,101)) -> int:
    """ Угадывает число опираясь на подсказки

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        search_range (tuple, optional): Диапазон поиска. Defaults to (1,101).

    Returns:
        int: Число опыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(search_range[0], search_range[1])  # предполагаемое число
        
        if predict_number == number:
            break  # выход из цикла если угадали
        elif number > predict_number: # если загаданное число больше то смещаем
            search_range = (predict_number, max(search_range))# диапазон в большую сторону
        elif number < predict_number:# если загаданное число меньше то смещаем
            search_range = (min(search_range), predict_number)# диапазон в меньшую сторону
            
    return count


def score_game(binary_predict, search_range: tuple = (1,101)) -> int:
    """ За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        binary_predict (_type_): Функция угадывания
        search_range (tuple, optional): Диапазан поиска. Defaults to (1,101).

    Returns:
        int: Среднее количество попвток
    """
    
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(search_range[0], search_range[1], size=(1000))  # загадали список чисел
    
    for number in random_array:
        count_ls.append(binary_predict(number, search_range))
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict_by_tips, (1,101))
