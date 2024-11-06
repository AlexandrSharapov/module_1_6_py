from calendar import Month

print('Работа со словарем')
my_st = {'Stepnaya': 22,
         'Rabochaya': 7,
         'Rechnaya': 25}
print(my_st)                                                     #Вывод словаря my_dict

print(my_st.get('Stepnaya', 'Такой улицы нет!'))                 #Вывод значения по существующему ключу
print(my_st.get('Gornaya', 'Такой улицы нет!'))                  #Вывод по отсутствующему ключу.

my_st.update({'Mayskaya': 112,
            'Naberegny': 59})                                   #Добавление нескольких ключей
print(my_st)

del my_st['Rechnaya']                                          #Удаление по существующему ключу из my_dict
print(my_st)



print('Работа с множествами')
my_set = {5, 5, 5, 7, 'Month', 0, 12, 12, 12, (6+6)}
print(my_set)

my_set.update('myset')                                          #добавление произвольных объектов
my_set.add(905)
print(my_set)

my_set.discard(5)
print(my_set)                                                   #Удаление элемента 5 из мmy_set