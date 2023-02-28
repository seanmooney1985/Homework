import sys



argc = len(sys.argv)



if argc > 1:
    print("Too many arguments!")
else:

    where = "Sky UK"
    age = "37"
    name = "sean"
    job = "Dev"


    if argc > 1:
        where = " and ".join(sys.argv[1:])


    print(f"Hello {name}! You are {age} years old and work as a {job} for {where}.")


    print("Goodbye from " + sys.argv[0] + "!")

