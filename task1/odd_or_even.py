'''
Створити функцію що приймає число, перевіряє його та виводить “Even” або “Odd”
'''


def oddOrEven(number):
    try:
        if number % 2 == 1:
            print("Odd")
        else:
            print("Even")
    except TypeError:
        print("This isn't a number!")

        
oddOrEven(10)
oddOrEven(7)
oddOrEven('text')
