import random
def zadacha1():
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    x =int(input('Введите число'))
    if x in s:
        print('Поздравляю, Вы угадали число!')
    else:
        print('Нет такого числа!')

def zadacha2():
    s1 = []
    s = [1 ,2 , 3, 4, 5, 5]
    for i in s:
        if s.count(i) > 1:
            if i not in s1:
                s1.append(i)
    print(*s1)

def zadacha3():
    day = ('Понедельник','Вторник','Среда','Четверг','Пятница' ,'Суббота','Воскресенье')
    s = int(input('Количество выходных?'))
    print('Ваши выходные дни:', *day[-s:])
    print('Ваши рабочие дни:', *day[:-s])

def zadacha4():
    group1=('иванов','соколов','семенов','сидоров','попов','романов','сергеев','пав','ывв','ыфвф')
    group2=('ячс', 'жжо','трр','иим','ххз','йц','нн','рпа','авывы','аыв')
    #a
    a1=[]
    a1.append(random.sample(group1,5))
    a2=[]
    a2.append(random.sample(group2,5))
    a=[]
    a.extend(*a1)
    a.extend(*a2)
    a=tuple(a)
    #b
    print(group1)
    print(group2)
    print(*a)
    #c
    print(len(a))
    #d
    print(*sorted(a))
    #e
    print('иванов' in a , a.count('иванов')))

zadacha1()
