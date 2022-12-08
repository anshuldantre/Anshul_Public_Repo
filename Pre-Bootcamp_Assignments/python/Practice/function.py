def addition (num1, num2):
    num3 = num1 + num2;
    return(num3)

x=addition(4,5)
print(x)


def add_string (str1):
    return ("Hi "+str1)

x=add_string("Anshul")
print(x)
x=add_string("Shradha")
print(x)
x=add_string("Dantres")
print(x)

def print_name(naam="", times=2):
    print(f"Good Morning {naam} \n" * times)
print_name("Anshul",1)
print_name("")
print_name("Dantres")
print_name(times=6)
print_name(times=3,naam="Shradha")