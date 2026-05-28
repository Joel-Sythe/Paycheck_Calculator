import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

hours_worked = int(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))

def calculate_pay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        overtime_hours = hours - 40
        return (40 * rate) + (overtime_hours * rate * 1.5)
    
pay = calculate_pay(hours_worked, hourly_rate)
print(f"The total pay is: ${pay:.2f}")

reave = input("Do you want to plot the pay vs hours worked? (yes/no): ")

if reave.lower() == 'yes':
    hours = np.arange(0, 60, 1)
    pays = [calculate_pay(h, hourly_rate) for h in hours]
    plot(hours, pays, "Pay vs Hours Worked", "Hours Worked", "Pay")



def plot(x, y, title, xlabel, ylabel):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def read_csv(file_path):
    data = pd.read_csv(file_path)
    return data

