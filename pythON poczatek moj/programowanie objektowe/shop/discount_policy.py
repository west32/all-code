
def standart_policy (total_prize):
    return total_prize

def loyal_policy (total_prize):
    return total_prize * 0.95

def christmas_policy(total_prize):
    if total_prize >100:
        return total_prize - 20
    return total_prize










