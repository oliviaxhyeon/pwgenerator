import string
import random
 
length_pw = 10 # the length of password
length_id = 12 # the length of Id

print("==============================================")
print(" 16 digits Id & 12 digits Password Generator")
print("==============================================")
print("\n* Upper Case:", string.ascii_uppercase)
print("* Lower Case:", string.ascii_lowercase)
print("* Number:", string.digits)
 
id_elements = string.ascii_letters + string.digits 

# Generated ID & Password
new_id = ""
for i in range(length_id):
  new_id += random.choice(id_elements)
print("\nID: ", new_id)

new_pw = ""
for i in range(length_pw):
  new_pw += random.choice(id_elements)
print("Password: ", new_pw)


# Generated ID & Password
new_id = ""
for i in range(length_id):
  new_id += random.choice(id_elements)
print("\nID: ", new_id)

new_pw = ""
for i in range(length_pw):
  new_pw += random.choice(id_elements)
print("Password: ", new_pw)


# Generated ID & Password
new_id = ""
for i in range(length_id):
  new_id += random.choice(id_elements)
print("\nID: ", new_id)

new_pw = ""
for i in range(length_pw):
  new_pw += random.choice(id_elements)
print("Password: ", new_pw)


# Generated ID & Password
new_id = ""
for i in range(length_id):
  new_id += random.choice(id_elements)
print("\nID: ", new_id)

new_pw = ""
for i in range(length_pw):
  new_pw += random.choice(id_elements)
print("Password: ", new_pw)


# Generated ID & Password
new_id = ""
for i in range(length_id):
  new_id += random.choice(id_elements)
print("\nID: ", new_id)

new_pw = ""
for i in range(length_pw):
  new_pw += random.choice(id_elements)
print("Password: ", new_pw)
