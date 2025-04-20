import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        rent = int(entry_rent.get())
        food = int(entry_food.get())
        electricity_units = int(entry_units.get())
        charge_per_unit = int(entry_charge.get())
        persons = int(entry_persons.get())

        total_bill = electricity_units * charge_per_unit
        per_person = (rent + food + total_bill) // persons

        result_label.config(text=f"Each person will pay: ₹{per_person}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

root = tk.Tk()
root.title("Roommate Bill Splitter")
root.geometry("350x400")
root.resizable(False, False)

tk.Label(root, text="Rent (₹):").pack(pady=5)
entry_rent = tk.Entry(root)
entry_rent.pack()

tk.Label(root, text="Food Cost (₹):").pack(pady=5)
entry_food = tk.Entry(root)
entry_food.pack()

tk.Label(root, text="Electricity Units:").pack(pady=5)
entry_units = tk.Entry(root)
entry_units.pack()

tk.Label(root, text="Charge per Unit (₹):").pack(pady=5)
entry_charge = tk.Entry(root)
entry_charge.pack()

tk.Label(root, text="Number of Persons:").pack(pady=5)
entry_persons = tk.Entry(root)
entry_persons.pack()

tk.Button(root, text="Calculate", command=calculate, bg="lightblue").pack(pady=20)

result_label = tk.Label(root, text="Each person will pay: ₹0", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
