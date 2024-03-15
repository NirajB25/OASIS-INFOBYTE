import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100  # converting height from cm to meters
    bmi = weight / (height ** 2)
    bmi_label.config(text="BMI: {:.2f}".format(bmi))

    interpretation = ""
    if bmi < 18.5:
        interpretation = "Underweight"
    elif 18.5 <= bmi < 25:
        interpretation = "Normal weight"
    elif 25 <= bmi < 30:
        interpretation = "Overweight"
    else:
        interpretation = "Obese"

    interpretation_label.config(text="Interpretation: {}".format(interpretation))

root = tk.Tk()
root.title("BMI Calculator")

# Create labels and entries for weight and height
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, sticky="e")

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(root, text="Height (cm):")
height_label.grid(row=1, column=0, sticky="e")

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

# Button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2)

# Label to display BMI
bmi_label = tk.Label(root, text="BMI: ")
bmi_label.grid(row=3, columnspan=2)

# Label to display interpretation
interpretation_label = tk.Label(root, text="Interpretation: ")
interpretation_label.grid(row=4, columnspan=2)

# Center align all widgets
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()