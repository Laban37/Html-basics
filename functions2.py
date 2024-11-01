def greet(age : int, school, name ="guest"):
    #     what function does
    print(f"hello,{name} you are {age} years old and school at {school} ")

# greet(name="joseph",age=10, school="emobilis")
# # greet("joseph")

def avr(number1 : int,number2 :int,number3:int):
    return(number1 + number2 +number3)/3

average =avr(45,76,84)
# print(average)

def avr(math : int,geo : int,bio : int):

    return (math + geo + bio )/3

average = avr(85,90,89)
# print(average)

def foo(z):
    return z if z <=1 else z * foo(z-1)

# print(foo(5))

def grade(average_marks):
    if 80<= average_marks <= 100:
        return "A"
    elif 70<= average_marks <80:
        return "B"
    elif 60<= average_marks <70:
        return "C"
    elif 50<= average_marks <60:
        return "D"
    elif 0<= average_marks <50:
        return "E"
    else:
        return "invalid marks"

print(grade(75))
def num(*args):
    return sum(args)

print(num(12,14,26))

def details(**kwargs):
    print(kwargs)

print(num(12,14,26))





