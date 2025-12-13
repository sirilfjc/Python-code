# Base class
class Device:
    
    # Method of Device class
    def power_on(self):
        print("Device is powering ON")

    # Method to be overridden
    def show(self):
        print("Basic Device Display")


# Child class inheriting Device
class Mobile(Device):

    # Method specific to Mobile
    def call(self):
        print("Calling from Mobile")

    # Overriding show() method
    def show(self):
        print("Mobile Screen Display")


# Child class inheriting Mobile (Multilevel Inheritance)
class Smartphone(Mobile):

    # Overriding show() method again
    def show(self):
        print("Smartphone Touch Display")


# -------- Driver Code --------

# Object of base class
d = Device()
d.power_on()     # Calls Device method
d.show()         # Calls Device show()

print()

# Object of Mobile class
m = Mobile()
m.call()         # Calls Mobile method
m.show()         # Calls overridden show() of Mobile

print()

# Object of Smartphone class
s = Smartphone()
s.show()         # Calls overridden show() of Smartphone
