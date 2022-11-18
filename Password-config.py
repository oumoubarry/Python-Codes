# Creating a users database
users_database = {
    "mariamb" : "Paris123",
    "ashleyj" : "Sydney256",
    "ObamaB" : "Tokyo22"
}

# Initializing users data

username_response = {}
password_response = {}
n = 0


#  starting the loop by entering the username and password

while n < 6 :
    username_response = input("User Name: ")
    password_response = input("Password:  ")
    n +=1

# Verifying if the username and password is correct

    if username_response in users_database  and users_database[username_response]==password_response :
        print("Login successful")
        break

# Continying the itiration when the password or username is incorrect up to 5 times 

    elif username_response not in users_database or users_database[username_response]!=password_response :
        if n <= 5:
            print("Access denied")

# Locking the account after five unsuccesful logins

        else:
            print("Account Locked, contact your Administrator") 
# Completing the iteration
    else:
        break
