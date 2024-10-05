# import
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import tkinter.messagebox

# main_window
main_window = tk.Tk()
Title = main_window.title("Currency Converter", )
main_window.geometry('750x420')

# frame
frame = tk.Frame(main_window, width=1500, height=800, bg='gray95', highlightbackground="turquoise4",
                 highlightcolor="turquoise4", highlightthickness=15)
frame.pack(pady=5, padx=5)

# Entry for amount
entry_label = tk.Label(frame, width=15, text="Enter amount :", font=("Times New Roman", 15, 'bold'), relief='groove',
                       bg='light cyan')
entry_label.grid(row=0, column=0, pady=20, padx=20)

entry_amount = ttk.Entry(frame, width=20, font=("Times New Roman", 15, 'bold'))
entry_amount.grid(row=0, column=1, pady=20, padx=20)

# label 1 (from currency)
l1 = tk.Label(frame, text="From currency :", width=15, font=("Times New Roman", 15, 'bold'), relief='groove',
              foreground="black", bg='light cyan')
l1.grid(row=1, column=0, pady=20, padx=20)

# combobox 1 (from currency)
n = tk.StringVar()
currency1 = ttk.Combobox(frame, width=20, textvariable=n)
currency1_values = pd.read_csv("curr_eurobase.csv")['curr_name'].tolist()
currency1['values'] = currency1_values
currency1.config(font=("Times New Roman", 15, 'bold'))
currency1.grid(row=1, column=1, padx=20)
# label 2 (to currency)
l2 = tk.Label(frame, text="Convert to :", width=15, font=("Times New Roman", 15, 'bold'), relief='groove',
              bg='light cyan')
l2.grid(row=2, column=0, pady=20, padx=20)

# combobox 2 (to currency)
k = tk.StringVar()
currency2 = ttk.Combobox(frame, width=20, textvariable=k)
currency2['values'] = currency1_values
currency2.grid(row=2, column=1, pady=20, padx=20)
currency2.config(font=("Times New Roman", 15, 'bold'))


# currency convertor functon
def convert_currency():
    try:
        # amount to a float
        convert_amt = float(entry_amount.get())
        result_label.config(fg='black')
    except ValueError:
        # If conversion fails, show an error message and return
        tkinter.messagebox.showwarning("Invalid Input",
                                       '''Invalid Input
                                                  Enter Number ''')

    data = pd.read_csv("curr_eurobase.csv")
    from_curr_name = currency1.get()
    to_curr_name = currency2.get()
    convert_amt = float(entry_amount.get())
    from_val = data[data.curr_name == from_curr_name]
    to_val = data[data.curr_name == to_curr_name]
    curr_name_list = data.curr_name.to_list()
    to_euro_list = data.to_euro.to_list()
    from_index_of_curr_name_list = curr_name_list.index(from_curr_name)
    to_index_of_curr_name_list = curr_name_list.index(to_curr_name)
    convert = (convert_amt * to_euro_list[to_index_of_curr_name_list]) / to_euro_list[from_index_of_curr_name_list]
    result_label.config(text=f"converted amount : {round(convert, 3)}")


# style for button
style = ttk.Style()
style.configure('W.TButton', font=('Times New Roman', 15, 'bold'), foreground='turquoise4', relief='raised')
style.map('W.TButton', foreground=[('active', '!disabled', 'red')],
          background=[('active', 'black')])

# Button for converting
button1 = ttk.Button(frame, text="Convert", style='W.TButton', command=convert_currency)
button1.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

# Result label
result_label = tk.Label(frame, width=30, font=("Times New Roman", 15, 'bold'), background='white', relief='groove')
result_label.grid(row=4, column=0, columnspan=2, pady=10, padx=10)


# Create a clear button
def clear_fields():
    entry_amount.delete(0, tk.END)
    currency1.set("")
    currency2.set("")
    result_label.config(text="")


clear_button = ttk.Button(frame, text="Clear all", style='W.TButton', command=clear_fields)
clear_button.grid(row=2, column=2, pady=20, padx=10, sticky='se')

# Button for closing window
button2 = ttk.Button(frame, text="Close", style='W.TButton', command=main_window.destroy)
button2.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

main_window.mainloop()
