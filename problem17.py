#Взять Лист №1 из Google Colab и посчитать сколько раз там встречается имя "Jack".
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
n=0
for i in names:
    if i == 'Jack':
        n+=1
print (n)
    