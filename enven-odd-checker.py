# Checking for Even or Odd
# Entering the number
user_number = int(input("Please enter a number between 1-100:  "))

# Defining the function
def even_odd_check(user_number):
    if (user_number % 2) ==0:
        print( "It is an even number".format(user_number))
    else:
        print("It is an odd number".format(user_number))

# Recalling the function
even_odd_check(user_number)
