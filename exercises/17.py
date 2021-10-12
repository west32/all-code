import random
import string

# Write a password generator in Python. Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be
# random, generating a new password every time the user asks for a new password. Include your run-time
# code in a main method.
#
# Extra:

def passwordGenerator():
    low_letters="abcdefghijklmnoprstuwxyz"
    upp_letters=low_letters.upper()
    symbols="`~!@#$%^&*()_+=\|]}[{;:',<.>/?"
    numbers="0123456789"
    all_digits= low_letters+upp_letters+symbols+numbers
    password= ""
    password += random.choice(low_letters)
    password += random.choice(upp_letters)
    password += random.choice(symbols)
    password += random.choice(numbers)
    for _ in range (4):
        password += random.choice(all_digits)

    password= set(password)
    password_str=""
    for element in password:
        password_str += element
    return password_str

print(passwordGenerator())

# or

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print (p)

#  or

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))

