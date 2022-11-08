# ##  Control Flow
num = int(input("what is your favorite number? : \n"))

if num < 0:
    print("negative")
elif num > 0:
    print("positive")
else:
    print("zero")

# Compare Three Numbers 

red_balls = int(input("enter how many red balls you have: "))
green_balls = int(input("enter how many green balls you have:  "))
yellow_balls = int(input ("enter how many yellow balls you have:  "))

if red_balls == green_balls and green_balls == yellow_balls:
    print(f"{red_balls} , {green_balls} , {yellow_balls} are equal ")

else: 
    print(f"{red_balls} , {green_balls} , {yellow_balls} are not equal ")

