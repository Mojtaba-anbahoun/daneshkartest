class Discount_Error(Exception):
    pass


def apply_discount(price, discount):
    final_price = int(price*(1 - discount))
    if not 0 <= final_price < price:
        raise Discount_Error("Invalid Discount")
    return final_price
