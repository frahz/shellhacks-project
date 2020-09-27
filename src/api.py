import requests
import json
import random
import datetime

apiKey = "2b6a3f2d6c0a4e58fe27c130bc198782"


def newCustomerId():
    global apiKey

    url = f"http://api.reimaginebanking.com/enterprise/accounts?key={apiKey}"

    response = requests.get(url)
    data = json.loads(response.text)
    results = data["results"]
    rand_index = random.randint(0, len(results) - 1)
    return results[rand_index]["customer_id"]


def getCustomerId():
    global apiKey

    acc_num = input("enter account number: ")

    url = f"http://api.reimaginebanking.com/accounts?key={apiKey}"
    response = requests.get(url)
    data = json.loads(response.text)
    for person in data:
        if acc_num in person["account_number"]:
            return person["_id"]
    else:
        return "ERROR: Account Number is incorrect"


def newCustomer():
    global apiKey

    acc_type = ["Credit Card", "Checking", "Savings"]
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    print("What type of account are you trying to open today:")
    print("1. Credit Card\n2. Checkings\n3. Savings\n0. Back")
    n = int(input())

    if n == 0:
        pass
    nickname = input("What nickname do you wish to give this account: ")
    customerId = newCustomerId()
    acc_num = "".join(random.choices(digits, k=16))
    url = f"http://api.reimaginebanking.com/customers/{customerId}/accounts?key={apiKey}"

    if n == 2 or n == 3:
        balance = int(input("How much do you want to deposit initially: "))

    payload = {
        "type": acc_type[n-1],
        "nickname": nickname,
        "rewards": 0,
        "balance": balance,
        "account_number": acc_num
    }
    r = requests.post(
        url,
        data=json.dumps(payload),
        headers={"content-type": "application/json"}
    )

    if r.status_code == 201:
        print('account created')
    else:
        print(r.status_code)


def deposit(amount, description):
    global apiKey

    customerId = "5f6fdfacf1bac107157e17fe"  # getCustomerId()
    # amount = int(input("How much do you want to deposit: "))
    # description = input("Add comment to deposit or leave empty if none: ")
    currentDay = datetime.date.today().isoformat()

    url = f"http://api.reimaginebanking.com/accounts/{customerId}/deposits?key={apiKey}"
    payload = {
        "medium": "balance",
        "transaction_date": currentDay,
        "status": "pending",
        "amount": amount,
        "description": None if description == "" else description
    }
    r = requests.post(
        url,
        data=json.dumps(payload),
        headers={"content-type": "application/json"}
    )

    if r.status_code == 201:
        print("deposit successful.")
    else:
        print("Sadge")


def withdraw(amount, description):
    global apiKey

    customerId = getCustomerId()
    # amount = int(input("How much do you want to withdraw: "))
    # description = input("Add comment to withdrawal or leave empty if none: ")
    currentDay = datetime.date.today().isoformat()

    url = f"http://api.reimaginebanking.com/accounts/{customerId}/withdrawals?key={apiKey}"
    payload = {
        "medium": "balance",
        "transaction_date": currentDay,
        "status": "pending",
        "amount": amount,
        "description": None if description == "" else description
    }
    r = requests.post(
        url,
        data=json.dumps(payload),
        headers={"content-type": "application/json"}
    )

    if r.status_code == 201:
        return "withdrawal successful."
    else:
        return "Sadge"


def loan():
    global apiKey
    loan_type = ["home", "auto", "small business"]
    currentDay = datetime.date.today().isoformat()
    loan_id = newCustomerId()

    customerId = getCustomerId()
    print("What type of loan are you trying to get today:")
    print("1. Home Loan\n2. Auto Loan\n3. Small Business Loan\n0. Back")
    n = int(input())

    creditScore = int(input("What is your current credit score: "))

    if n == 1 and creditScore < 720:
        return "Sorry, you are not currently eligble for a home loan."
    elif n == 2 and creditScore < 650:
        return "Sorry, you are not currently eligble for an auto loan."
    elif n == 3 and creditScore < 680:
        return "Sorry, you are not currently eligble for a small business loan."
    elif n == 0:
        pass

    amount = int(
        input(f"What is the total loan amount for the {loan_type[n-1]} loan: "))
    months = int(input(
        f"What do you want the duration of the {loan_type[n-1]} loan to be (in months): "))
    monthlyPayment = amount // months
    description = input("Add comment to loan or leave empty if none: ")

    url = f"http://api.reimaginebanking.com/accounts/{customerId}/loans?key={apiKey}"
    payload = {
        "type": loan_type[n-1],
        "status": "pending",
        "credit_score": creditScore,
        "monthly_payment": monthlyPayment,
        "amount": amount,
        "description": None if description == "" else description
    }

    r = requests.post(
        url,
        data=json.dumps(payload),
        headers={"content-type": "application/json"}
    )

    if r.status_code == 201:
        print("loan creation successful.")
    else:
        print("Sadge", r.status_code)
