#
# def standart_policy (total_prize):
#     return total_prize
#
# def loyal_policy (total_prize):
#     return total_prize * 0.95
#
# def christmas_policy(total_prize):
#     if total_prize >100:
#         return total_prize - 20
#     return total_prize
#










def standart_policy(total_prize):
    return total_prize

def loyal_policy(total_price):
    return total_price * 0.95

def christmas_policy(total_price):
    if total_price > 100:
        return total_price- 20
    return total_price


