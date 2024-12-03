# Tuto funkci implementuj.
def my_decorator(func):
    def do_three_times(*args, **kwargs):
        for i in range(1,4):
            print(f'{func.__name__} {i}/3')

            if i != 3:
                func(*args, **kwargs)
                
            else:
                returned = func(*args, **kwargs)
                if returned != None:
                    return returned


    return do_three_times






#  Testy:

@my_decorator
def add_numbers(a, b):
    return a + b
    
@my_decorator
def say_hello():
    print("Hello world!")

print(add_numbers(1, 3)) # add_numbers 1/3
                         # add_numbers 2/3
                         # add_numbers 3/3
                         # 4
                               
say_hello() # say_hello 1/3
            # Hello world!
            # say_hello 2/3
            # Hello world!
            # say_hello 3/3
            # Hello world!