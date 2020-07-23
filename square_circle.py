from math import pi as p

def square_footage():
    while True:
        length = input("What is the length of your room: (Please put a number) ")
        if length.replace('.', '', 1).isdigit()  == True:
            new_length = float(length)
            break
        else:
            print("You didn't put a number...")
            continue
        return new_length

    while True:
        width = input("What is the width of your room: (Please put a number) ")
        if length.replace('.', '', 1).isdigit()  == True:
            new_width = float(width)
            break
        else:
            print("You didn't put a number...")
            continue 
        return width
    
    area = new_length * new_width
    print(f"The area of the room is: {area}")


def circle_circum():
    diameter = input("What is the diameter of the circle?: (That's from one end to the other.)")
    new_diameter = float(diameter)
    
    circumference = p * new_diameter 
    print(f"The area of the circle is: {circumference}")


