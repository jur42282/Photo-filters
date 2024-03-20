from PIL import Image

def greenFilter(image):
    x  = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = image.getpixel((x,y))
            prumer = int((r+g+b)/2.4)
            image.putpixel((x,y), (r , b, r))
            if prumer > 150:
                image.putpixel((x,y), (255, 255, 255))
            else:
                image.putpixel((x,y), (100, 130, 90))
            y += 1
        x += 1
    image.show()
    print()

def blackAndWhite(image):
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = image.getpixel((x,y))
            prumer = int((r+g+b)/2.7)
            image.putpixel((x,y), (r , b, r))
            if prumer > 150:
                image.putpixel((x,y), (255, 255, 255))
            else:
                image.putpixel((x,y), (10, 8, 0))
            y += 1
        x += 1
    image.show()

def redFilter(image):
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
            r, g, b = image.getpixel((x,y))
            prumer = int((r+g+b)/2.7)
            image.putpixel((x,y), (r , b, r))
            if prumer > 150:
                image.putpixel((x,y), (255, 255, 255))
            else:
                image.putpixel((x,y), (200, 8, 0))
            y += 1
        x += 1
    image.show()

image = Image.open("kaves.png")
sirka, vyska = image.size
print("What filter would you like to apply to your image? (1, 2, 3)")
print("1. Green Filter")
print("2. Black and White Filter")
print("3. Red Filter")
uInput = input()
if uInput == "1":
    greenFilter(image)
elif uInput == "2":
    blackAndWhite(image)
elif uInput == "3":
    redFilter(image)
else:
    print("Invalid input. Please try again.")
    uInput = input()