outer = "Hello world"

def example_function(param):
    inner = "Hello function: {}".format(param) #only visible inside the function
    print(inner, outer)

example_function("first")
example_function("second")
print(inner)
