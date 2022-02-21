try:
    celsius = int(input("Temprature in celsius: "))
    farenhite = (celsius * (9/5) + 32)
    print(f"F & C Ratio- {farenhite/celsius}")
    print(farenhite)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Celsius canotbe zero")
