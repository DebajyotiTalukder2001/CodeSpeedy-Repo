
# import tkinter module
import tkinter as tk


# Define the balance variable
balance = 10000

# Create the main window
root = tk.Tk()
root.resizable(False, False)
root.geometry("700x510")
root.title("ATM Interface")
root.configure(bg="lightgray")

# Create the labels
label_1 = tk.Label(root, text="Welcome to the ATM", font='Helvetica 18 bold', bg="lightgray")


label_2 = tk.Label(root, text="Please select an option", font = "13", bg="lightgray")
label_3 = tk.Label(root, text="Enter the amount", font = 'Helvetica 13 bold', bg="lightgray")

# Create the buttons
button_1 = tk.Button(root, text="Withdraw Money", bg="green", fg="white",font = "8")
button_2 = tk.Button(root, text="Deposit Money", bg="yellow", fg="black",font = "8")
button_3 = tk.Button(root, text="Check Balance", bg="blue", fg="white",font = "8")
button_4 = tk.Button(root, text="Exit", bg="red", fg="white",font = "8", width="12")
button_5 = tk.Button(root, text="Clear", bg="gray", fg="black",font = "8", width="12")

# Create the text box
text_box = tk.Text(root, width= 40 , height= 5, bd="4", font="5")

# Create the entry box
entry_box = tk.Entry(root, width=50, font="7", bd="4")

# Pack the labels and buttons
label_1.place(x=225, y=20)
label_2.place(x=240, y=50)
button_1.place(x=50, y=100)
button_2.place(x=450, y=100)
button_3.place(x=50, y=180)
button_4.place(x=450, y=180)
button_5.place(x=255, y=180)
label_3.place(x=255, y=250)
entry_box.place(x=50, y=300)
text_box.place(x=120, y=350)

# Default value in the entry box. User can edit the value.
entry_box.insert(tk.END, "500")

# Print statements in the text box
def print_statement(statement):
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, statement)

# Withdraw money
def withdraw():
    text_box.delete("1.0", tk.END)
    amount = int(entry_box.get())
    global balance
    if amount <= balance:
        balance -= amount
        print("You have withdrawn {}.".format(amount))
        print_statement("You have withdrawn {}.".format(amount))
    else:
        print("Insufficient balance.")
        print_statement("Insufficient balance.")

# Deposit money
def deposit():
    text_box.delete("1.0", tk.END)
    amount = int(entry_box.get())
    global balance
    balance += amount
    print("You have deposited {}.".format(amount))
    print_statement("You have deposited {}.".format(amount))

# Check balance
def check_balance():
    text_box.delete("1.0", tk.END)
    print("Your balance is {}.".format(balance))
    print_statement("Your balance is {}.".format(balance))

# Clear text box
def clear_text_box():
    text_box.delete("1.0", tk.END)

# Add the clear_text_box() function to the button click events
button_1.config(command=withdraw)
button_2.config(command=deposit)
button_3.config(command=check_balance)
button_4.config(command=exit)
button_5.config(command=clear_text_box)

# Start the main loop
root.mainloop()
