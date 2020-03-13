
# single inheritance

class base_class:
    class_var = 90
    class_string = "base class string is cool!"
    def __init__(self):
        self.b_var = 45
        self.b_string = "Base class is cool!"
    
    def base_function1(self):
        print("This is base class function1")
    
    def base_function2(self):
        print("This is base class function2")
    
# ------------------------------------------

class derived_class(base_class):
    def __init__(self):
        self.d_var = 34
        self.d_string = "Derived class is also cool!"
    
    def derived_function(self):
        print("This is derived function")

    
base_object = base_class()
derived_object = derived_class()

base_object.base_function1()
base_object.base_function2()

derived_object.derived_function()

print(derived_object.d_string)
print(derived_object.d_var)

print(base_object.b_string)
print(base_object.b_var)

print(derived_object.class_string)
print(derived_object.class_var)
