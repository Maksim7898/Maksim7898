import tkinter as tk  #импортируем библиотеку tk
from tkinter import messagebox   #импортируем библиотеку  messagebox
from tkinter import filedialog  #импортируем библиотеку  filedialog

def update_result(value): #создаем функцию
    result_label.config(text=value)

def calculator(operation):#создаем функцию сложения и вычитания
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == 'add':
            result = num1 + num2 
            update_result(f"Результат:{result}")
        elif operation == 'subtract':
            result = num1 - num2
            update_result(f"Результат:{result}")

    except ValueError:
        update_result("Введите числовые значения")


def calculator1(operation):#создаем функцию умножения и деления
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == 'multiplication':
            result = num1 * num2
            update_result(f"Результат:{result}")
        elif operation == 'division':
            result = num1 / num2
            update_result(f"Результат:{result}")

    except ValueError:
        update_result("Введите числовые значения")

window = tk.Tk()
window.geometry("980x740")

entry1 = tk.Entry(window)
entry1.pack(pady=10)
entry1.insert(0, "1 число")
entry2 = tk.Entry(window)
entry2.pack(pady=10)
entry2.insert(0,"2 число")

plus_button = tk.Button(window, text="Сложить", command=lambda: calculator('add'))
plus_button.pack(pady=10)

minus_button = tk.Button(window, text="Вычесть", command=lambda: calculator('subtract'))
minus_button.pack(pady=10)

multiplication_button = tk.Button(window, text="Умножить", command=lambda: calculator1('multiplication'))
multiplication_button.pack(pady=10)

divison_button = tk.Button(window, text="Делить", command=lambda: calculator1('division'))
divison_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=40)
window.mainloop()



