# EXERCISE #4: AREA & VOLUME

# area(10, 4)  →  40 
# perimeter(10, 4)  →  28 
# volume(10, 4, 5)  →  200 
# surfaceArea(10, 4, 5)  →  220

def area(length, width):
    # Return the product of the length and width:
    return length * width

def perimeter(length, width):
    # Return the sum of the length twice and the width twice:
    return length + width + length + width

def volume(length, width, height):
    # Return the product of the length, width, and height:
    return length * width * height

def surfaceArea(length, width, height):
    # Return the sum of the area of each of the six sides:
    return (length * width * 2) + (length * height * 2) + (width * height * 2)

print(area(10, 10) == 100)
print(area(0, 9999) == 0)
print(area(5, 8) == 40)
print(perimeter(10, 10) == 40)
print(perimeter(0, 9999) == 19998)
print(perimeter(5, 8) == 26)
print(volume(10, 10, 10) == 1000)
print(volume(9999, 0, 9999) == 0)
print(volume(5, 8, 10) == 400)
print(surfaceArea(10, 10, 10) == 600)
print(surfaceArea(9999, 0, 9999) == 199960002)
print(surfaceArea(5, 8, 10) == 340)

