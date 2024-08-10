menu={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":100,
            "coffee":25,
        },
        "cost":150 
    },
    "expresso":{
        "ingredients":{
            "water":250,
            "milk":150,
            "coffee":230,
        },
        "cost":100 
    },
    "cappusino":{
        "ingredients":{
            "water":50,
            "milk":100,
            "coffee":35,
        },
        "cost":200 
    }
    
}
profit=0
resources= {
    "water":500,
    "milk":200,
    "coffee":100
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry! there is not enough{item}")
            return False
    return True  
  
def process_coin():
    print("Please insert coins")
    total=0
    coins_five=int(input("How many 5R coins?:: "))     
    coins_ten=int(input("How many 10Rs coins?: "))     
    coins_twenty=int(input("How many 20Rs coins?: "))   
    total= (coins_five* 5) +(coins_ten* 10) +(coins_twenty* 20) 
    return total
 
def is_payment_succesful(money,coffee_cost):
    if money>=coffee_cost:
        global profit
        profit +=coffee_cost 
        change  =money-coffee_cost
        print(f" Here is your Rs{change}in change")
        return True
    else:
        print("Sorry that's not enough money .Money refunded")
        return False
    
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item]-= coffee_ingredients[item]
    print(f" here is your {coffee_name}...Enjoy !!")      
        
is_on=True
while is_on:
 choise=input("what would you like to have?(latte/expresso/cappucino): ")
 if choise=="off":
     is_on=False
 elif choise=="report":
     print(f"water={resources['water']}ml")
     print(f"Milk={resources['milk']}ml")
     print(f"Coffee={resources['coffee']}g")
     print(f"Money=Rs{profit}")
 else:
     coffee_type=menu[choise]
     print(coffee_type)   
     if check_resources(coffee_type['ingredients']):
         payment=process_coin() 
         if is_payment_succesful(payment,coffee_type['cost']):
             make_coffee(choise,coffee_type['ingredients'])
     
 