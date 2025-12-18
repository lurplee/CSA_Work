velocity=0
angle_degrees=0
target_range=0
obj_mass=0
k_val=0
drawback=0

import my_calc as c

def header(msg):
    print(f"==================================\n{msg}\n==================================")


choice =1
use_calc = True


while choice in [1,2,3] and use_calc == True:
    header("Welcome to CATAPULT CALCULATOR")
    choice = int(input("[1] Range\n[2] Drawback \n[3] Angle\n"))
    
    if choice ==1:
        header("CALCULATING RANGE")
        header(f"ESTIMATED RANGE: {c.calc_range()} ")

    elif choice ==2:
        header("CALCULATING DRAWBACK")

        result = c.calc_drawback()

        if result != None:
            header(f"ESTIMATED DRAWBACK NEEDED: {result}")
        else:
            header(f"Sorry, there is no real drawback for the inputted values!")

    elif choice ==3:
        header("CALCULATING ANGLE")
        result = c.calc_angle()
        if result != None:
            header(f"ESTIMATED ANGLE NEEDED: {result[1]} Degrees ({result[0]} Rad)")
    

    use_calc = input("Calculate Another Value? [Y/N]\n").upper()
    if use_calc == "Y":
        use_calc = True
    else:
        use_calc = False

print("Thank you for using CATAPULT CALCULATOR!")

