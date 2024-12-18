import tkinter as tk  
from tkinter import messagebox  
from tkinter import filedialog  

def calculate_flight_time(distance, speed):
    """Вычисляет время полета на основе расстояния и скорости."""
    if speed <= 0: 
        raise ValueError("Скорость должна быть больше нуля.") 
    time = distance / speed
    return time  


def on_calculate(): 
    try:
        distance = float(distance_entry.get())  
        speed = float(speed_entry.get())  
        flight_time = calculate_flight_time(distance, speed)  
        messagebox.showinfo("Результат", f"Время полета: {flight_time:.2f} часов")  
    except ValueError as e:  
        messagebox.showerror("Ошибка", str(e))  


def on_exit():  
    root.quit()  

root = tk.Tk()  
root.title("Калькулятор времени полета")  
root.geometry("400x250")  
root.configure(bg="#f0f0f0") 


tk.Label(root, text="Расстояние (км):", bg="#f0f0f0").pack(pady=10)  
distance_entry = tk.Entry(root, width=20)  
distance_entry.pack(pady=5)  

tk.Label(root, text="Скорость (км/ч):", bg="#f0f0f0").pack(pady=10)  
speed_entry = tk.Entry(root, width=20)  
speed_entry.pack(pady=5)  

calculate_button = tk.Button(root, text="Рассчитать", command=on_calculate, bg="#4CAF50", fg="white") 
calculate_button.pack(pady=10)  #

exit_button = tk.Button(root, text="Выход", command=on_exit, bg="#f44336", fg="white")  
exit_button.pack(pady=10)  

root.mainloop()  



