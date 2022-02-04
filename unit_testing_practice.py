
<<<<<<< HEAD

def unit_testing_practice():
    first_tuple = [0,0]
    second_tuple = [2,2]

=======
def input_values():
    x1 , y1 = input("Please enter the first pair of the line without spaces")
    x2, y2 = input("Please enter the second pair of the line without spaces")
    x3 = input("Enter the x value for which the y value will be calculated")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    x3 = int(x3)
    slope_calculation(x1,y1,x2,y2,x3)
    return (x1,y1,x2,y2,x3)



def slope_calculation(x1,y1,x2,y2,x3):
    first = (x1,y1)
    second = (x2,y2)
    slope = (second[1]-first[1])/(second[0]-first[0])
    b = y1 -slope*x1
    line_calculation(slope, x3, b)
    return slope, b

def line_calculation(slope,x3,b):
    y3 = slope*x3 + b 
    print("The calculated y value is {} based on the x value {} ".format(y3,x3))
    return y3


if __name__ == "__main__":
    input_values()
>>>>>>> 69470584b8e4d8c1aabe42823dd4426fef12d30d
    
