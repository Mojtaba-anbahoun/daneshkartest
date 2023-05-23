class Discount_Error(Exception):
    pass

def integer_discount(function):
    def wrapper(price: int, discount:int)-> int:
        return function(price, discount/60)
    
    return wrapper

#result = integer_discount(apply_discount)(1000,30)
#print(result)
#print(apply_discount(1000,30))

@integer_discount
def apply_discount(price, discount):
    final_price = int(price*(1 - discount))
    if not 0 <= final_price < price:
        raise Discount_Error("Invalid Discount")
    return final_price

print(apply_discount(1000,30))

