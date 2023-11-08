import tkinter as tk

def evaluate_expression():
    try:
        expression = entry.get()
        expression = expression.replace('mod', '%').replace('^', '**')  # Replace 'mod' with '%' and '^' with '**'
        result_value = eval(expression)
        result.set(result_value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result_value))
    except Exception as e:
        result.set("Error")

def button_click(char):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + char)

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+',
    '(', ')', 'mod', '^'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, command=evaluate_expression).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row_val,
                                                                                                      column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=row_val, column=0, columnspan=4)

root.mainloop()
