from abc import ABC, abstractmethod

# ===================================================
# 1. ABSTRACTION
# ===================================================
# By inheriting from ABC (Abstract BAse Class), we make SmartDevice a blueprint.
# You cannot create an object directly from SmartDevice (e.g., device = SmartDevice("Thing")will throw an error).

class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name

        # ==========================================
        # 2. ENCAPSULATION
        # ==========================================
        # The double underscore (__) makes __is_on private. 
        # External code cannot do `my_light.__is_on = True`. 
        # It MUST use the turn_on() or turn_off() methods.
        self.__is_on = False

    # Public methods to safely interact with the private __is_on attribute
    def turn_on(self):
        self.__is_on = True
        print("f[{self.name}] has been turned ON.")

    def turn_off(self):
        self.__is_on = False
        print(f"[{self.name}] has been turned OFF.")

    # A safe "getter" method to check the status without modifying it
    def get_status(self):
        return self.__is_on
    
    # This is an Abstract Method. 
    # It forces every child class (like Light or AC) to create its own version of this method.
    @abstractmethod
    def device_info(self):
        pass


# ==========================================
# 3. INHERITANCE
# ==========================================
# SmartLight inherits all the properties (name) and methods (turn_on, turn_off) from SmartDevice.

class SmartLight(SmartDevice):
    def __init__(self, name, color = "White"):
        # super() calls the parent class's constructor to set up the 'name'
        super().__init__(name)
        self.color = color


    # ==========================================
    # 4. POLYMORPHISM
    # ==========================================
    # We are fulfilling the abstract method from the parent class, 
    # but giving it a specific implementation meant only for lights.

    def device_info(self):
        state = "ON" if self.get_status() else "OFF"
        return f" LIGHT  | Name: {self.name} | Power: {state} | Color: {self.color}"
    
# 3. INHERITANCE (Another child class)
class SmartAC(SmartDevice):
    def __init__(self, name, temperature=24):
        super().__init__(name)
        self.temperature = temperature

    # 4. POLYMORPHISM (Different behaviour for the same method name)
    def device_info(self):
        state = "ON" if self.get_status() else "OFF"
        return f" AC   | Name: {self.name} | Power: {state} | Temperature: {self.temperature}°C"
    

# ==========================================
# --- TESTING THE SYSTEM ---
# ==========================================

# Create specific objects (Instances)
living_room_light = SmartLight("Living Room Ceiling", color="Warm White")
bedroom_ac = SmartAC("Master Bedroom AC", temperature=22)

# Using Inherited methods (Encapsulation keeps the power state safe)
living_room_light.turn_on()
bedroom_ac.turn_on()

print("\n--- Smart Home Dashboard ---")

# Grouping different objects in a single list
my_home_devices = [living_room_light, bedroom_ac]

# Demonstrating Polymorphism: 
# We call the EXACT SAME method `device_info()` on every item in the list.
# Python automatically knows whether to run the Light's version or the AC's version.
for device in my_home_devices:
    print(device.device_info())
