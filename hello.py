def farenheit_to_celcius(farenheit):
    celcius=(farenheit-32)*5/9
    return celcius
farenheit=float(input("enter temperature in farenheit"))
celcius=farenheit_to_celcius(farenheit)
print(f"{farenheit}F={celcius:2f}C")
