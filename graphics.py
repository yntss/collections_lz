import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(-5, 6) #Задаём значения x
y = np.square(x) #y для y=x^2
y1 = np.exp(x) #y для y=e^x
x1=x[x>0] #Задаём значения x отдельно для ф-ии y=ln(x), т.к нат. логарифм не определяется для x<=0
y2 = np.log(x1) #y для y=ln(x)
y3 = x**3 #y для y=x^3
plt.title("График функций y=x^2, y=e^x, y=ln(x), y= x^3", color='#173554', fontstyle="italic", fontweight="bold") #Заголовок графика
plt.xlabel('Ось х', color='#173554', fontweight="bold") #Подпись для оси х
plt.ylabel('Ось y', color='#173554', fontweight="bold") #Подпись для оси y
plt.plot(x, y, color="#1A6DC1", marker='o', markersize=5, label='x^2') #Обозначаем как будет выглядеть каждая функция 
plt.plot(x, y1, color='#992145', marker='s', markersize=5, label='e^x')
plt.plot(x1, y2, color="#000000", marker='^', markersize=5, label='ln(x)') 
plt.plot(x, y3, color="#02F53E", marker='x', markersize=5, label='x^3')
plt.legend() #Легенда графика
plt.show() #Выводим график

