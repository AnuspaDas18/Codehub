def calculate_area(length,width):
    return length*width
def calculate_perimeter(length,width):
    return 2*(length+width)
length=float(input("Enter the length of a Rectangle:"))
width=float(input("Enter the width of a Rectangle:"))
area=calculate_area(length,width)
perimeter=calculate_perimeter(length,width)
print("The area of a Rectangle is:",area)
print("The area of a Rectangle is:",perimeter)
