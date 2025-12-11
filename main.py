import arithmetic
import geometry as geo

print("Hello World")

num1 = int(input("Enter num 1 : "))
num2 = int(input("Enter num 2 : "))

print("Add : ", arithmetic.add(num1,num2))

len = int(input("Enter length : "))
br = int(input("Enter breadth : "))

geo.cal_rect_area(len,br)
geo.cal_rect_peri(len,br)
