#John Wangwang RAID: Area Calculator

import math

def square(length: float):
    return length**2

def rectangle(length: float, width:float):
    return length*width

def triangle(base: float, height: float):
    return 1.0/2.0*base*height

def circle(radius: float):
    return math.pi*(radius**2)

def trapezoid(base_a: float, base_b: float, height: float):
    return ((base_a*base_b)/2)* height

def main():

    choice = int(input("""1. square
2. rectangle
3. triangle
4. circle
5. trapezoid
Enter the follow number to calculate the area of each one:"""))

    if choice not in [1,2,3,4,5]:
       
        print("Error Inccorrect input")
        return
    
    if choice == 1:

        length = float(input("Enter the length of a square:"))
        print(f"The Area of this square is {square(length):.2f}")

    if choice == 2:

        length = float(input("Enter the length of a rectangle:"))
        width = float(input("Enter the width of a rectangle:  "))

        print(f"The Area of this rectangle is {rectangle(length, width):.2f}") 

    if choice == 3:
        
        base = float(input("Enter the base of a triangle:    "))
        height = float(input("Enter the height of a triangle:"))

        print(f"The Area of this triangle is {triangle(base, height):.2f}") 

    if choice == 4:
        
        radius = float(input("Enter the radius of a circle:"))

        print(f"The Area of this circle is {circle(radius):.2f}") 
    
    else:

        base_a = float(input("Enter the first base of a trapezoid: "))
        base_b = float(input("Enter the second base of a trapezoid:"))
        height = float(input("Enter the height of a trapezoid:     "))

        print(f"The Area of this trapezoid is {trapezoid(base_a, base_b, height):.2f}") 


if __name__ == "__main__":
    main()