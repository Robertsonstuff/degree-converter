
def conv(num):
    return(9/5 * celsius + 32)

def convert(num):
    return((fahr - 32) * 5/9)

confirm = input("Are we converting celsius or fahrenheit today? ")

if confirm == 'celsius':
	celsius = int(input("What is the temperature we are coverting in celsius? "))
	fahrenheit = conv(celsius)
	print(f"{(round(fahrenheit))} degrees fahrenheit")
else:
    fahr = int(input("What is the temperature we are converting in fahrenheit? "))
    celsius = convert(fahr)
    print(f"{(round(celsius))} degrees celsius")
