var = input("Hello123:")


print("a) The value of var as upper case: " + var.upper())


print("b) The number of characters in var: ", len(var))


if any(char.isdigit() for char in var):
    print("c) Yes, var contains numeric characters.")
else:
    print("c) No, var does not contain numeric characters.")
