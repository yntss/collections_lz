import matplotlib.pyplot as plt
import numpy as np 

x = np.arange(-5, 6)
y = np.square(x)
y2 = np.log(x)
y3 = x**3
plt.title("График функции y=x^2", color='#173554', fontstyle="italic", fontweight="bold")
plt.xlabel('Ось х', color='#173554', fontweight="bold") #Подпись для оси х
plt.ylabel('Ось y', color='#173554', fontweight="bold")
plt.plot(x, y, color='#173554', marker='o', markersize=5)
plt.plot(y2, color='#992145', marker='|', markersize=5)
plt.plot(y3, color='#351024', marker='x', markersize=7)
plt.show()

