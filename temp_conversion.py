
def convert_100_to_celsius():
    # Convert a temperature of 100 degrees fahrenheit to celsius
    # Save this to a variable called celsius_100, and use print() to print out the value
    # Is the resulting temperature you get an integer or float?
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is
    celsiuis_100 =(100-32) * 5/9
    print(celsiuis_100)
    print('float')
convert_100_to_celsius()
    # It is a Float because it is a decimal

def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
    # Save this to a variable called celsius_0, and use print() to print out the value
    celsius_0 =(0 - 32) * 5/9
    print(celsius_0)
convert_0_to_celsius()

def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables
    print((34.2 - 32) * 5/9)
convert_34_2_to_celsius()
'''
#Now, can you convert back?
'''

def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    print((5 * 9/5) + 32)

convert_5_to_fahrenheit()

def hotter_temp():
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively
    print('30.2 degrees celsius')
hotter_temp()

def convert_to_celsius(num):
    print((num - 32) * 5/9)

def convert_to_farenheit(num):
    print((num * 9/5) + 32)

def temperature_converter(num, degrees):
    if degrees == 'farenheit':
        convert_to_celsius(num)
    elif degrees == 'celsius':
        convert_to_farenheit(num)

temperature_converter(32, 'celsius')