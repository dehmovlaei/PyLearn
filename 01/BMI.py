height = float(input("please Enter Your Height: "))
weight = float(input("please Enter Your Weight: "))
bmi = weight / (height * height)
if bmi < 18.5:
    print("underWeight")
elif    bmi <= 24.9:
    print("normalWeight")
elif 25 <= bmi <= 29.9:
    print("overWeight")
elif 30 <= bmi <= 34.9:
    print("Obesity")
elif 35 <= bmi <= 39.9:
    print("extremeObesity")