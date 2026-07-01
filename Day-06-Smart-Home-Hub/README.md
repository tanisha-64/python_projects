# 🏠 Smart Home Hub - Python OOP Project

A beginner-friendly Python project designed to demonstrate the real-world application of **Object-Oriented Programming (OOP)** concepts. This system simulates a smart home environment where you can manage different smart devices (like Lights and ACs) from a central hub.

## 🚀 Overview

This project doesn't just create devices; it enforces strict rules on how they operate using the four core pillars of Object-Oriented Programming. It acts as a perfect reference guide for anyone trying to understand how OOP works under the hood in Python.

## 🧠 OOP Concepts Implemented

1. **Abstraction (The Blueprint):** - Uses Python's `ABC` module to create a `SmartDevice` base class.
   - Enforces a rule: You cannot instantiate a raw "Smart Device", and every child device *must* have a `device_info()` method.
   
2. **Encapsulation (The Shield):** - Device power states (`__is_on`) are kept private.
   - Prevents external code from directly modifying the state. It can only be changed safely using `turn_on()` and `turn_off()` methods.

3. **Inheritance (Code Reusability):** - `SmartLight` and `SmartAC` inherit common attributes (like `name`) and behaviors (like turning on/off) from the `SmartDevice` parent class.
   - Saves time and avoids writing duplicate code.

4. **Polymorphism (Many Forms):** - Both the Light and the AC use the exact same method name: `device_info()`.
   - However, they return completely different, device-specific outputs when called.

## 🛠️ How to Run

1. Make sure you have **Python 3.x** installed on your system.
2. Clone or download this repository.
3. Open your terminal or command prompt.
4. Navigate to the folder where the file is saved.
5. Run the following command:
   ```bash
   python smart_home.py


## 📋 Example Output
[Living Room Ceiling] has been turned ON.
[Master Bedroom AC] has been turned ON.

--- Smart Home Dashboard ---
💡 LIGHT  | Name: Living Room Ceiling | Power: ON | Color: Warm White
❄️ AC     | Name: Master Bedroom AC | Power: ON | Temp: 22°C


## AUTHOR
Tanisha Gupta