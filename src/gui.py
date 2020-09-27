import tkinter
from tkinter import *
import api as shapi

# Start of GUI tkinter App
window = tkinter.Tk()


window.title("Bank App")
window.geometry('800x600')
window.configure(bg="light blue")


# Menu Functions
def forget_menu_screen():
    title.pack_forget()
    menu_question.pack_forget()
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
    button.pack_forget()
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
    menu.pack_forget()
    new_account_question1.pack_forget()
    option1.pack_forget()
    option2.pack_forget()
    option3.pack_forget()
    new_account_question2.pack_forget()
    nickname.pack_forget()
    new_account_question3.pack_forget()
    initial_deposit.pack_forget()
    btn_sbmt.pack_forget()


# Form Funtions
def withdraw_form():
    withdraw_question1.pack(side=TOP, expand=YES)
    first_input.pack(side=TOP, expand=YES)
    withdraw_question2.pack(side=TOP, expand=YES)
    second_input.pack(side=TOP, expand=YES)
    button.pack(side=TOP, expand=YES)
    menu.pack(side=TOP, expand=YES)


def loan_form():
    # home, auto, small business, loans
    loan_question1.pack(side=TOP, expand=YES)
    # home, auto, small business, loans input
    loan_input1.pack(side=TOP, expand=YES)
    loan_question2.pack(side=TOP, expand=YES)  # total amount of loan
    loan_input2.pack(side=TOP, expand=YES)  # total amount of loan input
    loan_question3.pack(side=TOP, expand=YES)  # length in months
    loan_input3.pack(side=TOP, expand=YES)  # length in months input
    loan_question4.pack(side=TOP, expand=YES)  # manually credit score
    loan_input4.pack(side=TOP, expand=YES)  # manually credit score input
    button_applyforloan.pack(side=TOP, expand=YES)
    menu.pack(side=TOP, expand=YES)


def deposit_form():
    deposit_question1.pack(side=TOP, expand=YES)
    dep_input1.pack(side=TOP, expand=YES)
    deposit_question2.pack(side=TOP, expand=YES)
    dep_input2.pack(side=TOP, expand=YES)
    button_dep.pack(side=TOP, expand=YES)
    menu.pack(side=TOP, expand=YES)


def new_account_form():
    new_account_question1.pack(anchor=CENTER, expand=YES)
    option1.pack()
    option2.pack()
    option3.pack()
    new_account_question2.pack(anchor=CENTER, expand=YES)
    nickname.pack(anchor=CENTER, expand=YES)
    new_account_question3.pack(anchor=CENTER, expand=YES)
    initial_deposit.pack(anchor=CENTER, expand=YES)
    btn_sbmt.pack(anchor=CENTER, expand=YES)
    menu.pack(anchor=CENTER, expand=YES)


# Account ID Functions
def account_num_prompt_for_checkings():
    account_num_for_checkings.pack(side=TOP, expand=YES)
    account_num_input_for_checkings.pack(side=TOP, expand=YES)
    account_num_button_for_checkings.pack(side=TOP, expand=YES)
    menu.pack(side=TOP, expand=YES)
    if account_num_input_for_checkings.get() == "":
        account_id = None
    else:
        account_id = account_num_input_for_checkings.get()


def account_num_prompt_for_savings():
    account_num_for_savings.pack(side=TOP, expand=YES)
    account_num_input_for_savings.pack(side=TOP, expand=YES)
    account_num_button_for_savings.pack(side=TOP, expand=YES)
    menu.pack(side=TOP, expand=YES)
    if account_num_input_for_savings == "":
        account_id = None
    else:
        account_id = account_num_input_for_savings.get()


def account_num_prompt_for_credit():
    account_num_for_credit.pack(side=TOP, expand=YES)
    account_num_input_for_credit.pack(side=TOP, expand=YES)
    account_num_button_for_credit.pack(side=TOP, expand=YES)
    menu.pack(side=TOP, expand=YES)
    if account_num_input_for_credit.get() == "":
        account_id = None
    else:
        account_id = account_num_input_for_credit.get()


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
    forget_checkings_options()
    forget_savings_options()
    withdraw_form()


def loan_clicked():
    forget_menu_screen()
    loan_form()


def deposit_clicked():
    forget_menu_screen()
    forget_checkings_options()
    forget_savings_options()
    forget_credit_options()
    deposit_form()


def new_account_clicked():
    forget_menu_screen()
    new_account_form()


def withdraw_submit_amount_clicked():
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


def loan_submit_amount_clicked():
    if loan_input1.get() == "" or loan_input2.get() == "" or loan_input3.get() == "" or loan_input4.get() == "":
        error_message = tkinter.Label(
            window, text="Invalid entry!...Returning to home page!")
        error_message.pack()
        error_message.pack_forget
        window.after(2000, error_message)

    else:
        loan_type = str(loan_input1.get())
        loan_amount = int(loan_input2.get())
        loan_months = int(loan_input3.get())
        credit_score = int(loan_input4.get())
        pls = shapi.loan(amount=loan_amount, _type=loan_type,
                         months=loan_months, creditScore=credit_score)
        label = tkinter.Label(text=pls)
        label.pack()


# Forget Account Number Prompt Screen Functions
def forget_prompt_checkings():
    account_num_for_checkings.pack_forget()
    account_num_input_for_checkings.pack_forget()
    account_num_button_for_checkings.pack_forget()
    menu.pack_forget()


def forget_prompt_savings():
    account_num_for_savings.pack_forget()
    account_num_input_for_savings.pack_forget()
    account_num_button_for_savings.pack_forget()
    menu.pack_forget()


def forget_prompt_credit():
    account_num_for_credit.pack_forget()
    account_num_input_for_credit.pack_forget()
    account_num_button_for_credit.pack_forget()
    menu.pack_forget()

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


def forget_new_account_options():
    new_account_question1.pack_forget()
    option1.pack_forget()
    option2.pack_forget()
    option3.pack_forget()
    new_account_question2.pack_forget()
    nickname.pack_forget()
    btn_sbmt.pack_forget()

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


# Title
title = tkinter.Label(text="Welcome to our Banking App",
                      font=("Times", 30), bg="light blue")
title.pack(side=TOP)

menu_question = tkinter.Label(
    text="What type of account do you have?", font=("Times", 22), bg="light blue")
menu_question.pack(side=TOP)

# Menu Screen Buttons
bt1 = tkinter.Button(text='Credit Card', width=15,
                     height=2, command=credit_card_clicked)
bt1.pack(side=TOP, expand=YES)
bt2 = tkinter.Button(text='Checkings', width=15,
                     height=2, command=checkings_clicked)
bt2.pack(side=TOP, expand=YES)
bt3 = tkinter.Button(text='Savings', width=15,
                     height=2, command=savings_clicked)
bt3.pack(side=TOP, expand=YES)
bt = tkinter.Button(window, text="New Account", width=10,
                    height=1, command=new_account_clicked)
bt.config(anchor=CENTER)
bt.pack()

# New Account Form, Account type, Nickname, Intial Deposit
new_account_question1 = tkinter.Label(
    window, text="What type of account are you trying to open today?\n 1. Credit Card 2. Checkings 3.Savings", font=("Times", 14), bg='white')
new_account_question1.pack(side=TOP, expand=YES)
new_account_question1.pack_forget()

option1 = tkinter.Radiobutton(window, text='Credit Card', value='1')
option1.pack()
option1.pack_forget()
option2 = tkinter.Radiobutton(window, text='Checkings ', value='2')
option2.pack()
option2.pack_forget()
option3 = tkinter.Radiobutton(window, text='Savings  ', value='3')
option3.pack()
option3.pack_forget()

new_account_question2 = tkinter.Label(
    window, text="What nickname do you wish to give this account? ", font=("Times", 14), bg='white')
new_account_question2.pack(anchor=CENTER)
new_account_question2.pack_forget()

nickname = tkinter.Entry(window)
nickname.pack(anchor=CENTER)
nickname.pack_forget()

new_account_question3 = tkinter.Label(
    window, text="How much will your initial deposit be? ", font=("Times", 14), bg='white')
new_account_question3.pack(anchor=CENTER)
new_account_question3.pack_forget()

initial_deposit = tkinter.Entry(window)
initial_deposit.pack(anchor=CENTER)
initial_deposit.pack_forget()

btn_sbmt = tkinter.Button(text='Submit', width=10,
                          height=2, command=new_account_form)
btn_sbmt.pack(anchor=CENTER, expand=YES)
btn_sbmt.pack_forget()


# Credit Card Menu
bt1_for_credit = tkinter.Button(
    text='Loan (Still Not Setup)', width=15, height=2, command=deposit_clicked)
bt1_for_credit.pack(side=TOP, expand=YES)
bt1_for_credit.pack_forget()

bt2_for_credit = tkinter.Button(
    text='Menu', width=15, height=2, command=remember_menu_screen)
bt2_for_credit.pack(side=TOP, expand=YES)
bt2_for_credit.pack_forget()


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
    window, text="How much do you want to withdraw?", font=("Times", 18), bg='white')
withdraw_question1.pack(anchor=CENTER, expand=YES)
withdraw_question1.pack_forget()

first_input = tkinter.Entry(window)
first_input.pack(anchor=CENTER)
first_input.pack_forget()

withdraw_question2 = tkinter.Label(
    window, text="Add comment to withdrawal or leave empty if none. ", font=("Times", 18), bg='white')
withdraw_question2.pack(anchor=CENTER)
withdraw_question2.pack_forget()

second_input = tkinter.Entry(window)
second_input.pack(anchor=CENTER)
second_input.pack_forget()

button = tkinter.Button(text='Submit', width=10, height=2,
                        command=withdraw_submit_amount_clicked)
button.pack(anchor=CENTER, expand=YES)
button.pack_forget()

# Account Num Prompt for Checkings
account_num_for_checkings = tkinter.Label(
    window, text="Please Enter your Account Number Below.", font=("Times", 18),  bg='white')
account_num_for_checkings.pack(anchor=CENTER, expand=YES)
account_num_for_checkings.pack_forget()

account_num_input_for_checkings = tkinter.Entry(window)
account_num_input_for_checkings.pack(anchor=CENTER)
account_num_input_for_checkings.pack_forget()

account_num_button_for_checkings = tkinter.Button(
    text='Submit', width=10, height=2, command=checkings_menu_transition)
account_num_button_for_checkings.pack(anchor=CENTER, expand=YES)
account_num_button_for_checkings.pack_forget()

menu = tkinter.Button(text='Menu', width=15, height=2,
                      command=remember_menu_screen)
menu.pack(side=TOP, expand=YES)
menu.pack_forget()

# Account Num Prompt for Savings
account_num_for_savings = tkinter.Label(
    window, text="Please Enter your Account Number Below.", font=("Times", 18), bg='white')
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
    window, text="Please Enter your Account Number Below.", font=("Times", 18), bg='white')
account_num_for_credit.pack(anchor=CENTER, expand=YES)
account_num_for_credit.pack_forget()

account_num_input_for_credit = tkinter.Entry(window)
account_num_input_for_credit.pack(anchor=CENTER)
account_num_input_for_credit.pack_forget()

account_num_button_for_credit = tkinter.Button(
    text='Submit', width=10, height=2, command=credit_card_menu_transition)
account_num_button_for_credit.pack_forget()


# Deposit Form
deposit_question1 = tkinter.Label(
    window, text="How much do you want to deposit?", font=("Times", 18), bg="white")
deposit_question1.pack(anchor=CENTER, expand=YES)
deposit_question1.pack_forget()

dep_input1 = tkinter.Entry(window)
dep_input1.pack(anchor=CENTER)
dep_input1.pack_forget()

deposit_question2 = tkinter.Label(
    window, text="Add comment to deposit or leave empty if none. ", font=("Times", 18), bg='white')
deposit_question2.pack(anchor=CENTER)
deposit_question2.pack_forget()

dep_input2 = tkinter.Entry(window)
dep_input2.pack(anchor=CENTER)
dep_input2.pack_forget()

button_dep = tkinter.Button(text='Submit', width=10, height=2,
                            command=withdraw_submit_amount_clicked)
button_dep.pack(anchor=CENTER, expand=YES)
button_dep.pack_forget()


# Loan Form
loan_question1 = tkinter.Label(
    window, text="Would you like to apply for a home, auto, or   small business loan?", font=("Times", 18), bg='white')
deposit_question1.pack(anchor=CENTER, expand=YES)
deposit_question1.pack_forget()

loan_input1 = tkinter.Entry(window)
loan_input1.pack(anchor=CENTER)
loan_input1.pack_forget()

loan_question2 = tkinter.Label(
    window, text="How much would you like to take out the loan   for?", font=("Times", 18), bg='white')
deposit_question1.pack(anchor=CENTER, expand=YES)
deposit_question1.pack_forget()
loan_input2 = tkinter.Entry(window)
loan_input2.pack(anchor=CENTER)
loan_input2.pack_forget()

loan_question3 = tkinter.Label(
    window, text="How many months would you like to take the     loan out for?", font=("Times", 18), bg='white')
deposit_question1.pack(anchor=CENTER, expand=YES)
deposit_question1.pack_forget()
loan_input3 = tkinter.Entry(window)
loan_input3.pack(anchor=CENTER)
loan_input3.pack_forget()

loan_question4 = tkinter.Label(
    window, text="Please type in your Credit Score so that we    can evaluate your eligibilty for this loan.", font=("Times", 18), bg='white')
deposit_question1.pack(anchor=CENTER, expand=YES)
deposit_question1.pack_forget()
loan_input4 = tkinter.Entry(window)
loan_input4.pack(anchor=CENTER)
loan_input4.pack_forget()

button_applyforloan = tkinter.Button(text='Apply for Loan', width=20, height=5,
                                     command=loan_submit_amount_clicked)
button_applyforloan.pack(anchor=CENTER, expand=YES)
button_applyforloan.pack_forget()


window.mainloop()
