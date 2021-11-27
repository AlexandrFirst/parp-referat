try:
    1 / 0
except ZeroDivisionError:
    print("You can't divide by zero")
except ArithmeticError:
    print("Other arithmetic error")
except:
    print("Unknown exception")
else:
    print("Calculations are successful")
finally:
    print("Calculations are over")
