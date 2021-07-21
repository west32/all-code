# Utwórz zmienną value oraz instrukcję warunkową, która sprawdzi czy wartość tej zmiennej jest:
#
# True
# False
# None
# inną wartością

value = "True"
value_true= value == "True"
print(f"czy value = True?\t\t {value_true}")
value_false = value == "False"
print(f"czy value = False? \t\t {value_false}")
value_none = value == "None"
print(f"czy value = None?\t\t {value_none}")
value_other= value == 4.12
print(f"czy value = 4.12? \t\t {value_other}")