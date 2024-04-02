from PIL import Image
import filters

while True:
    img = input("Enter the name of the picture: ")
    try:
        image = Image.open(img)
        print("Image loaded successfully.")
        sirka, vyska = image.size
        break
    except FileNotFoundError:
        print("File not found. Please try again. Make sure you're entering the correct name of the picture and the file type.")

while True:
    print("What filter would you like to apply to your image? (1, 2, 3)")
    print("1. Green Filter")
    print("2. Black and White Filter")
    print("3. Red Filter")
    uInput = input()
    if uInput == "1":
        filters.greenFilter(image, sirka, vyska)
        break
    elif uInput == "2":
        filters.blackAndWhite(image, sirka, vyska)
        break
    elif uInput == "3":
        filters.redFilter(image, sirka, vyska)
        break
    else:
        print("Invalid input. Please try again.")
        continue
print("Done!")