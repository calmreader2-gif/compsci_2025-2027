
def discount_calculate(basket_value):
    discount_total = basket_value * 0.1
    return discount_total

print(discount_calculate(500))

def discount_check(basket_value):
    if basket_value > 100: 
        return True
    else:
        return False
    
def shopping_experience(basket_value):
    total_cost = basket_value
    if discount_check(basket_value):
        discount_total = discount_calculate(basket_value)
        total_cost = basket_value - discount_total
    return total_cost   
print(shopping_experience(150))
print(shopping_experience(78))





def member_discount(basket_value):
    member_discount = basket_value * 0.8
    return member_discount

is_member = True

def total_price (basket_value):
    total_price = basket_value
    return basket_value
    

def membership_discount(basket_value, is_member):
    total_price = basket_value
    if is_member:
        discount_total = member_discount(basket_value)
        total_price = discount_total
    return total_price

print(membership_discount(200, True))
print(membership_discount(200, False))





    
    
