def rectangle_cals(length,width):
    perimeter = 2*(length+width)
    

    area = length*width
   
    return f"The perimeter of the rectangle is {perimeter}\nThe area of the rectangle is {area} "


length = float(input("Enter the length of the rectangle here: "))

width = float(input("Enter the width of the rectangle here: "))


cals = rectangle_cals(length,width)

print(cals)