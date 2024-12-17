# team1_num = 5  # команда 1
# team2_num = 6  # команда 2
# score_1 = 40  # команда Мастер кода 5
# score_2 = 42  # команда Волшебники данных 6
# team1_time = 1552.512
# team2_time = 2153.31451
# tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'

# def challenge_result1():
#     if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
#         result = ‘Победа команды Мастера кода!’
#     elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
#         result = ‘Победа команды Волшебники Данных!’
#     else:
#         result = ‘Ничья!’

# # Переменные: количество участников первой команды (team1_num)
# print('В команде Мастера кода участников: %s !' % team1_num)
# # Переменные: количество участников в обеих командах (team1_num, team2_num)
# print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
#
# # Переменные: количество задач решённых командой 2 (score_2)
# print('Команда Волшебники данных решила задач: {}'.format(score_2), '!')
# # Переменные: время за которое команда 2 решила задачи (team1_time)
# print('Волшебники данных решили задачи за {}'.format(team1_time * 42 / 6), 'с !')
#
# # Переменные: количество решённых задач по командам: score_1, score_2
# print(f'Команды решили {score_1} и {score_2} задач.')
# # Переменные: исход соревнования (challenge_result)
# print(f'Результат битвы: {challenge_result}!')
# # Переменные: количество задач (tasks_total) и среднее время решения (time_avg)
#
# print('1 komanda', round(40 / 5 * 2153.31451, 1))  # 5 участников, решили 40 з, за team2_time = 2153.31451
# print('2 komanda', round(42 / 6 * 1552.512, 1))  # 6 участников, решили 42 з, за team1_time = 1552.512
# a = 40 / 5 * 2153.31451
# b = 42 / 6 * 1552.512
# # a = 40 / 5 * 2153.31451
# # b = 42 / 6 * 1552.512
# print((a + b) / 82)
# print()
#
#
# print()
# print()

""" а """
# участники, кол-во участников

team1_num = 5  # "Мастер кода", 5 уч.
team2_num = 6  # "Волшебники данных", 6 уч.

# количество задач решённых командой
score_1 = 40  # команда Мастер кода 5
score_2 = 42  # команда Волшебники данных 6

# время за которое команда 2 решила задачи
team1_time = 1552.512  # "Волшебники данных"
team2_time = 2153.31451  # "Мастер кода"
# tasks_total = 82  # всего задач
# time_avg = 45.2  # среднее время решения
# challenge_result = ''

# результат
# if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
#     print('Победа команды Мастера кода!')
# elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
#     print('Победа команды Волшебники Данных!')
# else:
#     print('Ничья!')

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    return result


# участники, кол-во участников
print('В команде Мастера кода участников: %s !' % team1_num)
print('В команде команды Волшебники Данных: %s !' % team2_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

# кол-во задач и время
time_tasks_1 = team2_time * score_1 / team1_num  # Время на задачи 1 команды
time_task1_1 = time_tasks_1 / score_1  # Время на 1 задачу 1 команды
print('Команда Мастера кода решила задач: {}'.format(score_1), '!')
print('Команда Мастера кода решила задачи за {}'.format(time_tasks_1), 'с !')
# print(time_task1_1)
time_tasks_2 = team1_time * score_2 / team2_num  # Время на задачи 2 команды
time_task1_2 = time_tasks_2 / score_2  # Время на 1 задачу 2 команды
print('Команда Волшебники данных решила задач: {}'.format(score_2), '!')
print('Команда Волшебники данных решила задачи за {}'.format(time_tasks_2), 'с !')
# print(time_task1_2)
print(f'Команды решили {score_1} и {score_2} задач.')


print(challenge_result())
tasks_total = score_1 + score_2  # 82 адачи
time_avg = time_task1_1 + time_task1_2  # среднее время на 1 задачу
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
