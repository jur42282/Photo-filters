from PIL import Image
image = Image.open("káves.png")
sirka, vyska = image.size

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
