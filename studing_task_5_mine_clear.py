from random import randint
from time import time

# Игра в сапера: 
#     1. модуль приветствия и возврата игры - со статистикой
#     2. главный модуль игры - упареления отрисовкой и ходами игрока
#     3. модуль расстановки мин компьютром
#     4. модуль хода игрока
#     5. модуль отрисовки поля
    

# модуль расстановки мин компьютером
def module_computer_position_mine(fd, num = 14):
    list_position = {}
    for i in range(1, 17):
        list_position[i] = []
    while num > 0:
        a = randint(1, 16)
        b = randint(1, 30)
        if b in list_position[a]:
            pass
        else:
            list_position[a].append(b)
            num -= 1
    # print(list_position)
    for i in list_position:
        for j in list_position[i]:
            fd[i][j] = 11
    # print(fd)
    return fd

# модуль получения хода игрока
def module_gamer_moves():

    # проверка хода инрока
    def checking_gamers(step):
        result_list = []
        result = ''
        mina = False
        if step[:4] in ['МИНА', 'мина', 'VBYF', 'vbyf', 'mina']:
            mina = True
            step =  step[4:]
        step = step.split('-')
        for i, num in enumerate(step):
            try: 
                if int(num):
                    result_list.append(num)
            except ValueError:
                print('Введено не верное значение')
                return True, 'a', 'b'
        if len(result_list) != 2:
            print('Вы неправильно ввели данные')
            return True, 'a', 'b'
        if int(result_list[0]) > 0 and int(result_list[0]) < 17:
            if int(result_list[1]) > 0 and int(result_list[1]) < 31:
                pass
        else:
            print('Вы указали не верный диапазон')
            return True, 'a', 'b'
        
        return False, result_list, mina
        
    # цикл получения значения
    def cycle_gamer_moves():
        password = True
        while password:
            step_number = input(f'''Сделайте ваш ход (например : 16-1 или 1-30) сначала вертикальная координата потом горизонтальная.
        ЕСЛИ хотите сделать отметку о мине перед цифрами набирите МИНА (например : МИНА8-15) если снять то же самое (МИНА8-15)
            \n''').lower()
            password, gemer_move, mina = checking_gamers(step_number)
        for i, elem in enumerate(gemer_move):
            gemer_move[i] = int(elem)   
        return gemer_move, mina
    
    return cycle_gamer_moves() 

# функция определени символа
def symbol_print(num):
    result =  '   '
    if num == 1:
        result = ' 1 '
    elif num == 2:
        result = ' 2 '
    elif num == 3:
        result = ' 3 '
    elif num == 4:
        result = ' 4 '
    elif num == 5:
        result = ' 5 '
    elif num == 6:
        result = ' 6 '
    elif num == 7:
        result = ' 7 '
    elif num == 8:
        result = ' 8 '
    elif num == 9:
        result = ' 9 '
    elif num == 10 or num == 11:
        result = ' o '
    elif num == 20 or num == 21:
        result = 'min'
    return result

# модуль проверки хода и распечатки поля
def module_pole_print(field_dict, key=False):
    count = 0
    str_1 = ['  ','1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    print('-'.join(str_1)) #первая строка 
    if key == True:  # вскрытие поля в случае подрава
        stop_timers = time()
        str_2 = f''
        for i in range(1, 17):
            if len(str(i)) == 1:
                str_2 = f'{str_2} {str(i)}'
            else:
                str_2 = f'{str_2}{str(i)}'
            for j in range(1, 31):
                if field_dict[i][j] == 11 or field_dict[i][j] == 21:                  
                    str_2 = f'{str_2} W '
                else:
                    str_2 = f'{str_2}{symbol_print(field_dict[i][j])}'  
            print(str_2) 
            str_2 = f''  
        return field_dict, stop_timers, 'мёртв'   
         
    else:    # прорисовка обычного поля
        str_2 = f''
        for i in range(1, 17):
            if len(str(i)) == 1:
                str_2 = f'{str_2} {str(i)}'
            else:
                str_2 = f'{str_2}{str(i)}'
            for j in field_dict[i]:
                str_2 = f'{str_2}{symbol_print(field_dict[i][j])}'
                if field_dict[i][j] in [10, 20]:
                    count += 1
            print(str_2)
            str_2 = f''
    
    print()
    print(f'Вам осталось: {count} полей.')
    if count == 0:
        stop_timers = time()
        return field_dict, stop_timers, 'жив'
    return field_dict, 0, '' 
    
# модуль расчета поля попадания и окружающих его полей
def module_for_calculating_players_move(fd, gm, key):
    
    if key == True:  # проверка на мины
        if fd[int(gm[0])][int(gm[1])] == 10:
            fd[int(gm[0])][int(gm[1])] = 20
        elif fd[int(gm[0])][int(gm[1])] == 11:
            fd[int(gm[0])][int(gm[1])] = 21
        elif fd[int(gm[0])][int(gm[1])] == 21:
            fd[int(gm[0])][int(gm[1])] = 11
        else:  
            fd[int(gm[0])][int(gm[1])] = 10
        return fd, False
    
    if fd[int(gm[0])][int(gm[1])] == 11:
        return fd, True
    # проверка на подрыв
    
    
    
    if fd[(gm[0])][(gm[1])] == 10:
        f_dict = {}
        while gm != []:
            y = gm[0]
            x = gm[1]
            count = 0
            
            if f_dict == {}:
                for e in range(1, 17):
                    f_dict[e] = []
            for i in range(y-1, y+2):
                if i > 0 and i < 17:
                    for j in range(x-1, x+2):
                        if j > 0 and j < 31:
                            if fd[i][j] == 11 or fd[i][j] == 21:
                                count +=1             
            fd[y][x] = count
            if count == 0: 
                for i1 in range(y-1, y+2):
                    if i1 > 0 and i1 < 17:
                        if i1 not in f_dict:
                            f_dict[i1] = []
                        for j1 in range(x-1, x+2):
                            if j1 > 0 and j1 < 31:
                                if j1 in f_dict[i1]:
                                    pass
                                elif fd[i1][j1] < 10:
                                    pass
                                else:
                                    f_dict[i1].append(j1)
            gm.clear()                      
            c_dict = {}
            c_dict = f_dict.copy()
            for k in c_dict:
                if c_dict[k] == []:
                    f_dict.pop(k)
                else: 
                    gm.append(k)
                    gm.append(c_dict[k][0])
                    f_dict[k] = c_dict[k][1:]
                    break
            # print(f_dict)  
    return fd, False

# главный модуль игры - управления 
def the_main_module_of_the_program(field_dict):
    field_dict = module_computer_position_mine(field_dict)
    start_timers = time()
    count = 0
    module_pole_print(field_dict)
    cycle_main_modul = True
    while cycle_main_modul:
        gem_move, key = module_gamer_moves() # ход игрока в виде списка цифр по вертикали и горизонту
        field_dict, key = module_for_calculating_players_move(field_dict, gem_move, key)
        field_dict, stop_time, death = module_pole_print(field_dict, key)
        count += 1
        if stop_time != 0:
            stop_time = int(stop_time - start_timers)
            cycle_main_modul = False 
    return True, count, death, stop_time 
    
# главный цикл перезапуска программы
def general_cycle_of_the_program():
    field_dict = {}
    for i in range(1, 17):
        field_dict[i] = {}
        for j in range (1, 31):
            field_dict[i][j] = 10
    password, count_geme, death, stop_time = the_main_module_of_the_program(field_dict)
    count = 1
    while password:
        if death == 'мёртв':
            cycle_word = input(f"""Поражение, Вы подарвались за {stop_time} секунд на {count_geme}попытке.  
Для продолжения нажмите ввод, если хотите выйти из игры введите любой знак:""")   
        else:
            cycle_word = input(f"""В этой игре Вы победили Вам потребовалось {stop_time} секунд и {count_geme} попыток!
Если Вы хотите продолжить нажмите ввод, если хотите выйти из игры введите любой знак:""")   
        if cycle_word != '':
            password = False
        else:
            field_dict = {}
            for i in range(1, 17):
                field_dict[i] = {}
                for j in range (1, 31):
                    field_dict[i][j] = 10
            password, count_geme, death, field_dict = the_main_module_of_the_program(field_dict)   
            count += 1
    
    return count

# модуль приветствия 
def start_program():  
    print(f'''
        Игра: Сапер поле 16х30 - при указании координат указывать через дефис например 16-30 или 1-1 
Если Вы готовы нажмите ввод, если хотите выйти из игры введите любой знак.''')
    enter_word = input('')
    if enter_word != '':
        print('Всего хорошего!')
    else:
        count = general_cycle_of_the_program()
        
    print(f'Вы закончили игру и Вы сыграли {count} раз. Всего хорошего!')

if __name__ == '__main__':
    start_program()