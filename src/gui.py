import tkinter
from tkinter import *
import api as shapi

# Start of GUI tkinter app
window = tkinter.Tk()


window.title("Bank App")
window.geometry('800x600')
window.configure(bg="light blue")

# Menu Functions


def forget_menu_screen():
    bt1.pack_forget()
    bt2.pack_forget()
    bt3.pack_forget()
    bt.pack_forget()


def remember_menu_screen():
    title.pack(side=TOP)
    menu_question.pack(side=TOP)
    bt1.pack(side=TOP, expand=YES)
    bt2.pack(side=TOP, expand=YES)
    bt3.pack(side=TOP, expand=YES)
    bt.pack(side=TOP, expand=YES)
    withdraw_question1.pack_forget()
    withdraw_question2.pack_forget()
    first_input.pack_forget()
    button_withdraw.pack_forget()
    account_num_for_checkings.pack_forget()
    account_num_for_savings.pack_forget()
    account_num_for_credit.pack_forget()
    account_num_input_for_checkings.pack_forget()
    account_num_button_for_checkings.pack_forget()
    account_num_input_for_savings.pack_forget()
    account_num_button_for_savings.pack_forget()
    account_num_input_for_credit.pack_forget()
    account_num_button_for_credit.pack_forget()
    bt1_for_credit.pack_forget()
    bt2_for_credit.pack_forget()
    bt1_for_checkings.pack_forget()
    bt2_for_checkings.pack_forget()
    bt3_for_checkings.pack_forget()
    bt1_for_savings.pack_forget()
    bt2_for_savings.pack_forget()
    bt3_for_savings.pack_forget()
    second_input.pack_forget()
    deposit_question1.pack_forget()
    dep_input1.pack_forget()
    deposit_question2.pack_forget()
    dep_input2.pack_forget()
    button_dep.pack_forget()


# Form Funtions
def withdraw_form():
    withdraw_question1.pack(side=TOP, expand=YES)
    first_input.pack(side=TOP, expand=YES)
    withdraw_question2.pack(side=TOP, expand=YES)
    second_input.pack(side=TOP, expand=YES)
    button_withdraw.pack(side=TOP, expand=YES)


def loan_form():
    pass


def deposit_form():
    deposit_question1.pack(side=TOP, expand=YES)
    dep_input1.pack(side=TOP, expand=YES)
    deposit_question2.pack(side=TOP, expand=YES)
    dep_input2.pack(side=TOP, expand=YES)
    button_dep.pack(side=TOP, expand=YES)


def new_account_form():
    pass


# Account ID Functions

def account_num_prompt_for_checkings():
    # global account_id
    if account_num_input_for_checkings.get() == "":
        account_id = None
    else:
        account_id = account_num_input_for_checkings.get()
    account_num_for_checkings.pack(side=TOP, expand=YES)
    account_num_input_for_checkings.pack(side=TOP, expand=YES)
    account_num_button_for_checkings.pack(side=TOP, expand=YES)


def account_num_prompt_for_savings():
    # global account_id
    if account_num_input_for_savings == "":
        account_id = None
    else:
        account_id = account_num_input_for_savings.get()
    account_num_for_savings.pack(side=TOP, expand=YES)
    account_num_input_for_savings.pack(side=TOP, expand=YES)
    account_num_button_for_savings.pack(side=TOP, expand=YES)


def account_num_prompt_for_credit():
    # global account_id
    if account_num_input_for_credit.get() == "":
        account_id = None
    else:
        account_id = account_num_input_for_credit.get()
    account_num_for_credit.pack(side=TOP, expand=YES)
    account_num_input_for_credit.pack(side=TOP, expand=YES)
    account_num_button_for_credit.pack(side=TOP, expand=YES)
# Click Functions


def credit_card_clicked():
    forget_menu_screen()
    account_num_prompt_for_credit()


def checkings_clicked():
    forget_menu_screen()
    account_num_prompt_for_checkings()


def savings_clicked():
    forget_menu_screen()
    account_num_prompt_for_savings()


def withdraw_clicked():
    forget_menu_screen()
    withdraw_form()


def loan_clicked():
    forget_menu_screen()
    loan_form()


def deposit_clicked():
    forget_menu_screen()


def new_account_clicked():
    forget_menu_screen()


def withdraw_submit_amount_clicked():
    # global amount, description
    if first_input.get() == "":
        amount = None
    else:
        amount = int(first_input.get())
    description = second_input.get()
    pls = shapi.withdraw(amount=amount, description=description)
    label = tkinter.Label(text=pls)
    label.pack()


def deposit_submit_amount_clicked():
    if dep_input1.get() == "":
        amount = None
    else:
        amount = int(dep_input1.get())
    description = dep_input2.get()
    pls = shapi.deposit(amount=amount, description=description)
    label = tkinter.Label(text=pls)
    label.pack()

# Forget Account Number Prompt Screen Functions


def forget_prompt_checkings():
    account_num_for_checkings.pack_forget()
    account_num_input_for_checkings.pack_forget()
    account_num_button_for_checkings.pack_forget()


def forget_prompt_savings():
    account_num_for_savings.pack_forget()
    account_num_input_for_savings.pack_forget()
    account_num_button_for_savings.pack_forget()


def forget_prompt_credit():
    account_num_for_credit.pack_forget()
    account_num_input_for_credit.pack_forget()
    account_num_button_for_credit.pack_forget()

# More Forget Functions


def forget_checkings_options():
    bt1_for_checkings.pack_forget()
    bt2_for_checkings.pack_forget()
    bt3_for_checkings.pack_forget()


def forget_savings_options():
    bt1_for_savings.pack_forget()
    bt2_for_savings.pack_forget()
    bt3_for_savings.pack_forget()


def forget_credit_options():
    bt1_for_credit.pack_forget()
    bt2_for_credit.pack_forget()

# Checkings and Savings Menu Functions After Id input


def checkings_menu_transition():
    forget_prompt_checkings()
    bt1_for_checkings.pack(side=TOP, expand=YES)
    bt2_for_checkings.pack(side=TOP, expand=YES)
    bt3_for_checkings.pack(side=TOP, expand=YES)


def savings_menu_transition():
    forget_prompt_savings()
    bt1_for_savings.pack(side=TOP, expand=YES)
    bt2_for_savings.pack(side=TOP, expand=YES)
    bt3_for_savings.pack(side=TOP, expand=YES)


def credit_card_menu_transition():
    forget_prompt_credit()
    bt1_for_credit.pack(side=TOP, expand=YES)
    bt2_for_credit.pack(side=TOP, expand=YES)


# Checkings and Savings Menu Functions After Id input
def checkings_menu_transition():
    pass


def savings_menu_transition():
    pass


def credit_card_menu_transition():
    pass


# Title
title = tkinter.Label(text="Welcome to our banking App",
                      font=("Arial Bold", 30), bg="light blue")
title.pack(side=TOP)

menu_question = tkinter.Label(text="What type of account do you have?", font=(
    "Arial Bold", 22), bg="light blue")
menu_question.pack(side=TOP)

# Menu Screen Buttons
bt1 = tkinter.Button(text='Credit Card', width=15,
                     height=2, command=credit_card_clicked)
bt1.pack(side=TOP, expand=YES)
bt2 = tkinter.Button(text='Checkings', width=15, height=2)
bt2.pack(side=TOP, expand=YES)
bt3 = tkinter.Button(text='Savings', width=15, height=2)
bt3.pack(side=TOP, expand=YES)
bt = tkinter.Button(window, text="New Account", width=10,
                    height=1, command=withdraw_clicked)
bt.config(anchor=CENTER)
bt.pack()

# Credit Card Menu
bt1_for_credit = tkinter.Button(
    text='Deposit', width=15, height=2, command=deposit_clicked)
bt1_for_credit.pack(side=TOP, expand=YES)
bt1_for_credit.pack_forget()

bt2_for_credit = tkinter.Button(
    text='Menu', width=15, height=2, command=remember_menu_screen)
bt2_for_credit.pack(side=TOP, expand=YES)
bt2_for_credit.pack_forget()

# New Account Forms, Account type, Nickname, Intial Deposit


# Checkings Menu
bt1_for_checkings = tkinter.Button(
    text='Deposit', width=15, height=2, command=deposit_clicked)
bt1_for_checkings.pack(side=TOP, expand=YES)
bt1_for_checkings.pack_forget()

bt2_for_checkings = tkinter.Button(
    text='Withdraw', width=15, height=2, command=withdraw_clicked)
bt2_for_checkings.pack(side=TOP, expand=YES)
bt2_for_checkings.pack_forget()

bt3_for_checkings = tkinter.Button(
    text='Menu', width=15, height=2, command=remember_menu_screen)
bt3_for_checkings.pack(side=TOP, expand=YES)
bt3_for_checkings.pack_forget()

# Savings Menu
bt1_for_savings = tkinter.Button(
    text='Deposit', width=15, height=2, command=deposit_clicked)
bt1_for_savings.pack(side=TOP, expand=YES)
bt1_for_savings.pack_forget()

bt2_for_savings = tkinter.Button(
    text='Withdraw', width=15, height=2, command=withdraw_clicked)
bt2_for_savings.pack(side=TOP, expand=YES)
bt2_for_savings.pack_forget()

bt3_for_savings = tkinter.Button(
    text='Menu', width=10, height=2, command=remember_menu_screen)
bt3_for_savings.pack(side=TOP, expand=YES)
bt3_for_savings.pack_forget()

# Withdraw Form
withdraw_question1 = tkinter.Label(
    window, text="How much do you want to withdraw?", bg='white')
withdraw_question1.pack(anchor=CENTER, expand=YES)
withdraw_question1.pack_forget()

first_input = tkinter.Entry(window)
first_input.pack(anchor=CENTER)
first_input.pack_forget()

withdraw_question2 = tkinter.Label(
    window, text="Add comment to withdrawal or leave empty if none. ", bg='white')
withdraw_question2.pack(anchor=CENTER)
withdraw_question2.pack_forget()

second_input = tkinter.Entry(window)
second_input.pack(anchor=N)
second_input.pack_forget()

button_withdraw = tkinter.Button(text='Submit', width=10, height=2,
                                 command=withdraw_submit_amount_clicked)
button_withdraw.pack(anchor=CENTER, expand=YES)
button_withdraw.pack_forget()

# Deposit Form
deposit_question1 = tkinter.Label(
    window, text="How much do you want to deposit?", bg="white")
deposit_question1.pack(anchor=CENTER, expand=YES)
deposit_question1.pack_forget()

dep_input1 = tkinter.Entry(window)
dep_input1.pack(anchor=CENTER)
dep_input1.pack_forget()

deposit_question2 = tkinter.Label(
    window, text="Add comment to deposit or leave empty if none. ", bg='white')
deposit_question2.pack(anchor=CENTER)
deposit_question2.pack_forget()

dep_input2 = tkinter.Entry(window)
dep_input2.pack(anchor=N)
dep_input2.pack_forget()

button_dep = tkinter.Button(text='Submit', width=10, height=2,
                            command=withdraw_submit_amount_clicked)
button_dep.pack(anchor=CENTER, expand=YES)
button_dep.pack_forget()

# Loan Form
# withdraw_question1 = tkinter.Label(window, text="How much do you want to withdraw?", bg='white')
# withdraw_question1.pack(anchor=CENTER, expand=YES)
# withdraw_question1.pack_forget()

# first_input = tkinter.Entry(window)
# first_input.pack(anchor=CENTER)
# first_input.pack_forget()

# withdraw_question2 = tkinter.Label(window, text="Add comment to withdrawal or leave empty if none. ", bg='white')
# withdraw_question2.pack(anchor=CENTER)
# withdraw_question2.pack_forget()

# second_input = tkinter.Entry(window)
# second_input.pack(anchor=N)
# second_input.pack_forget()

# button = tkinter.Button(text='Submit', width=10, height=2, command=withdraw_submit_amount_clicked)
# button.pack(anchor=CENTER, expand=YES)
# button.pack_forget()

# Account Num Prompt for Checkings
account_num_for_checkings = tkinter.Label(
    window, text="Please Enter your Account Number Below.", bg='white')
account_num_for_checkings.pack(anchor=CENTER, expand=YES)
account_num_for_checkings.pack_forget()

account_num_input_for_checkings = tkinter.Entry(window)
account_num_input_for_checkings.pack(anchor=CENTER)
account_num_input_for_checkings.pack_forget()

account_num_button_for_checkings = tkinter.Button(
    text='Submit', width=10, height=2, command=checkings_menu_transition)
account_num_button_for_checkings.pack(anchor=CENTER, expand=YES)
account_num_button_for_checkings.pack_forget()

# Account Num Prompt for Savings
account_num_for_savings = tkinter.Label(
    window, text="Please Enter your Account Number Below.", bg='white')
account_num_for_savings.pack(anchor=CENTER, expand=YES)
account_num_for_savings.pack_forget()

account_num_input_for_savings = tkinter.Entry(window)
account_num_input_for_savings.pack(anchor=CENTER)
account_num_input_for_savings.pack_forget()

account_num_button_for_savings = tkinter.Button(
    text='Submit', width=10, height=2, command=savings_menu_transition)
account_num_button_for_savings.pack(anchor=CENTER, expand=YES)
account_num_button_for_savings.pack_forget()

# Account Num Prompt for Credit Card
account_num_for_credit = tkinter.Label(
    window, text="Please Enter your Account Number Below.", bg='white')
account_num_for_credit.pack(anchor=CENTER, expand=YES)
account_num_for_credit.pack_forget()

account_num_input_for_credit = tkinter.Entry(window)
account_num_input_for_credit.pack(anchor=CENTER)
account_num_input_for_credit.pack_forget()

account_num_button_for_credit = tkinter.Button(
    text='Submit', width=10, height=2, command=credit_card_menu_transition)
account_num_button_for_credit.pack(anchor=CENTER, expand=YES)
account_num_button_for_credit.pack_forget()


window.mainloop()
