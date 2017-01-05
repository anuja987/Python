inp = raw_input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 0.5 / 0.9
    print cel
except:
    print("Please input a number")
