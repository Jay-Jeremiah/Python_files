def circle(rad):
    pi = 3.14
    circumference = 2*pi*rad

    area = pi*rad*rad

    return f"The circumference of a circle is {round(circumference,4)}\n\nThe area of the circle is {round(area,4)}"

radius = float(input("Enter the radius of the circle here: "))

cals = circle(radius)

print(cals)
