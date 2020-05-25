num2 = 45.99
try:
    num2 + num3
    import mathematics
    num2 = mathematics.floor(num2)
except ModuleNotFoundError:
    print('Module does not exist, invent it')
except:
    print('An error was encountered')
