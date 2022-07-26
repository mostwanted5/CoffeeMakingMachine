MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = {
    "earned": 0,
}

def report(water, milk, coffee, cash):
    return f"water\t:\t{water}ml\nmilk\t:\t{milk}ml\ncoffee\t:\t{coffee}g\nmoney\t:\t${cash}"

def resource_check(order, water, milk, coffee):
    if(order == "espresso"):
        if(water < 50 or coffee < 18):
            return True
        else:
            return False
    elif(order == "latte"):
        if(water < 200 or milk < 150 or coffee < 24):
            return True
        else:
            return False
    elif(order == "cappuccino"):
        if(water < 250 or milk < 100 or coffee < 24):
            return True
        else:
            return False

def payment(quarters, dimes, nickles, pennies):
    cash_pay = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return cash_pay
def balance_cash(order, quarters, dimes, nickles, pennies):
    if(order=="espresso" and payment(quarters, dimes, nickles, pennies)>1.5):
        cash_balance=payment(quarters, dimes, nickles, pennies)-1.5
        print (f"You balance cash is {cash_balance}")
    elif (order == "latte" and payment(quarters, dimes, nickles, pennies) > 2.5):
        cash_balance = payment(quarters, dimes, nickles, pennies) - 2.5
        print (f"You balance cash is {cash_balance}")
    elif (order == "cappuccino" and payment(quarters, dimes, nickles, pennies) > 3):
        cash_balance = payment(quarters, dimes, nickles, pennies) - 3
        print (f"You balance cash is {cash_balance}")

def make_coffee():
    end_of_task=False
    while(not end_of_task):
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        cash = money["earned"]
        order = input("What would you like: Expresso, Latte, or Cappuccino: ").lower()
        if (order == "report"):
            print(report(water, milk, coffee, cash))
        else:
            if(order == "espresso"):
                resource_check(order=order, water=water, milk=milk, coffee=coffee)
                if(resource_check(order=order, water=water, milk=milk, coffee=coffee)==False):
                    quarters = float(input("Enter quarter amount: "))
                    dimes = float(input("Enter dimes amount: "))
                    nickles = float(input("Enter nickles amount: "))
                    pennies = float(input("Enter pennies amount: "))
                    if(payment(quarters, dimes, nickles, pennies)>=1.5):
                        water = resources["water"] = water - 50
                        coffee = resources["coffee"] = coffee - 18
                        cash = money["earned"] = cash + 1.5
                        print("Enjoy your espresso!")
                        balance_cash(order, quarters, dimes, nickles, pennies)
                    else:
                        print("Your cash is not sufficient, cash refunded")
                else:
                    print("Sorry, resources are not enough to proceed with your request")

            elif(order == "latte"):
                resource_check(order=order, water=water, milk=milk, coffee=coffee)
                if(resource_check(order=order, water=water, milk=milk, coffee=coffee) == False):
                    quarters = float(input("Enter quarter amount: "))
                    dimes = float(input("Enter dimes amount: "))
                    nickles = float(input("Enter nickles amount: "))
                    pennies = float(input("Enter pennies amount: "))
                    if(payment(quarters, dimes, nickles, pennies) >= 2.5):
                        water = resources["water"] = water - 200
                        milk = resources["milk"] = milk - 150
                        coffee = resources["coffee"] = coffee - 24
                        cash = money["earned"] = cash + 2.5
                        print("Enjoy your latte!")
                        balance_cash(order, quarters, dimes, nickles, pennies)
                    else:
                        print("Your cash is not sufficient, cash refunded")
                else:
                    print("Sorry, resources are not enough to proceed with your request")
            elif(order == "cappuccino"):
                (resource_check(order=order, water=water, milk=milk, coffee=coffee))
                if(resource_check(order=order, water=water, milk=milk, coffee=coffee) == False):
                    quarters = float(input("Enter quarter amount: "))
                    dimes = float(input("Enter dimes amount: "))
                    nickles = float(input("Enter nickles amount: "))
                    pennies = float(input("Enter pennies amount: "))
                    if(payment(quarters, dimes, nickles, pennies) >= 3):
                        water = resources["water"] = water - 250
                        milk = resources["milk"] = milk - 100
                        coffee = resources["coffee"] = coffee - 24
                        cash = money["earned"] = cash + 3
                        print("Enjoy your cappuccino!")
                        balance_cash(order, quarters, dimes, nickles, pennies)
                else:
                    print("Sorry, resources are not enough to proceed with your request")
            else:
                end_of_task=True
            make_coffee()
make_coffee()