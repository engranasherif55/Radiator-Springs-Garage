#  Radiator Springs Garage Management System

A Python command-line (CLI) application built using Object-Oriented Programming (OOP) concepts to manage a vehicle garage fleet.

---
##  Key Features

* **Object-Oriented Architecture:** 
  * Uses a base `Car` class with specialized `Racer` and `SupportVehicle` subclasses.
  * Implements Encapsulation using `@property` getters and setters to validate age, speed, and capacity.
* **Data Persistence:** Automatically saves and loads garage state to/from a `garage_data.json` file.
* **Error Handling:** Protects against invalid user input (non-numeric values, negative numbers) using `try-except` blocks.

---

##  Class Overview

* **`Car` (Base Class):** Holds common attributes like Car Number, Name, Age, Team, Speed, and Capacity.
* **`Racer`:** Extends `Car` to include `Races_Completed` and `Laps_Completed`, with a custom performance score calculation.
* **`SupportVehicle`:** Extends `Car` to include `Crew_Size` and `Reliability_Rating`, with its own performance score formula.

---

##  How to Run

1. Make sure Python 3.x is installed.
2. Open your terminal in the project directory.
3. Run the application:
   ```bash
   python Garage.py
