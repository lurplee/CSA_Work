import math
# Calculates DRAWBACK
def calc_drawback():
    angle_degrees = float(input("Angle (Degrees): "))
    range = float(input("Target Range (m): "))
    obj_mass = float(input("Mass of Object (kg): "))
    k_val = float(input("K-value (N/m): "))

    drawback = math.sqrt(9.8*range*obj_mass/k_val*(math.sin(math.radians(2*angle_degrees))))
    return(round(drawback,2))


# Converts K-VALUE -> INTIAL VELOCITY
def k_or_vel():
    user_choice = int(input("Will you be using\n[1] K-Value\n[2] Intial Velocity\n"))
    if user_choice ==1:
        k_val = float(input("K-Value (N/m): "))
        drawback = float(input("Drawback (m): "))
        obj_mass = float(input("Mass of Object (kg): "))
        velocity = math.pow(drawback,2)*(math.sqrt(k_val/obj_mass))
        
    elif user_choice ==2:
        velocity = float(input("Velocity: "))
    
    return(velocity)


#Calculating RANGE
def calc_range():

    velocity = k_or_vel()
    angle_degrees = float(input("Degrees: "))

    range = (math.pow(velocity,2)*math.sin(math.radians(2*angle_degrees)))/9.8
    if range > 0:
        return(round(range,2))


# Calculating ANGLE
def calc_angle():
    velocity = k_or_vel()
    range = float(input("Estimated/Actual Range (m): "))

    try:
        angle_radians = 0.5 * math.asin((range * 9.8)/ math.pow(velocity,2))
        angle_degrees = math.degrees(angle_radians)
        return(round(angle_radians,2), round(angle_degrees,2))
    except:
        print(f"Sorry, there is no real angle that would yield a velocity of {velocity} m/s and range of {range} m!")