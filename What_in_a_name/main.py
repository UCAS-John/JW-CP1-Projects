#John Wangwang RAID: What's in a name?

#calculate the area of rectangle or rhombus
def calculate_area(length, width):
    return length * width

#calculate the area of cube or cuboid
def calculate_volume(length, width, height):
    area = calculate_area(length, width)
    return area * height

length = 5
width = 3
area = calculate_area(length, width)
print(f"The flat thing's size is: {area}")

length_f = 4
width_f = 6
height = 2
volume = calculate_volume(length_f, width_f, height)
print(f"The big thing's size is: {volume}")
