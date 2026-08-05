import json
import os

print("RADIATOR SPRINGS GARAGE MANAGEMENT SYSTEM")
class Car:
    def __init__(self, Car_Number:int, Full_Name:str, Age:int, Racing_Team:str,Speed:float, Capacity:float):
        self._Car_Number = Car_Number
        self.Full_Name = Full_Name
        self.Age = Age
        self.Racing_Team = Racing_Team
        self.Speed = Speed
        self.Capacity = Capacity

    @property
    def Car_Number(self):
        return self._Car_Number
    
    @property
    def Age(self):
        return self._Age
    
    @property
    def Speed(self):
        return self._Speed
    @property
    def Capacity(self):
        return self._Capacity

    @Age.setter
    def Age(self, value):
        if value <= 0:
            raise ValueError
        self._Age=value

    @Speed.setter
    def Speed(self, value):
        if value <= 0:
            raise ValueError
        self._Speed=value

    @Capacity.setter
    def Capacity(self, value):
        if value <= 0:
            raise ValueError
        self._Capacity=value
    @property
    def performance_score(self):
        raise NotImplementedError("Subclasses must implement this method")

    def display(self):
        print(f"Car Number: {self.Car_Number}")
        print(f"Full Name: {self.Full_Name}")
        print(f"Age: {self.Age}")
        print(f"Racing Team: {self.Racing_Team}")
        print(f"Speed: {self.Speed}")
        print(f"Capacity: {self.Capacity}")
    
class Racer(Car):
    def __init__ (
            self,
            Car_Number:str,
            Full_Name:str,
            Age:int,
            Racing_Team:str,
            Speed:float,
            Capacity:float,
            Races_Completed:int,
            Laps_Completed:int,
        ):
        super().__init__(
            Car_Number, Full_Name, Age, Racing_Team, Speed, Capacity
        )

        self.Races_Completed = Races_Completed
        self.Laps_Completed = Laps_Completed
        
    @property
    def performance_score(self):
        return (self.Speed * 10) + (self.Capacity * 1)

    def to_dict(self):
        return{
            "type":"Racer",
            "Car_Number":self.Car_Number,
            "Full_Name":self.Full_Name,
            "Age":self.Age,
            "Racing_Team":self.Racing_Team,
            "Speed":self.Speed,
            "Capacity":self.Capacity,
            "Races_Completed":self.Races_Completed,
            "Laps_Completed":self.Laps_Completed
        }


    
class SupportVehicle(Car):
    def __init__ (
             self,
             Car_Number:str,
             Full_Name:str,
             Age:int,
             Racing_Team:str,
             Speed:float,
             Capacity:float,
             Crew_Size:int,
             Reliability_Rating:float,
        ):
        super().__init__(
            Car_Number, Full_Name, Age, Racing_Team, Speed, Capacity
        )
        self.Crew_Size=Crew_Size
        self.Reliability_Rating=Reliability_Rating
    @property
    def performance_score(self):
        return(self.Speed * 5) + (self.Capacity * 5)

    def to_dict(self):
        return{
            "type": "SupportVehicle",
            "Car_Number":self.Car_Number,
            "Full_Name":self.Full_Name,
            "Age":self.Age,
            "Racing_Team":self.Racing_Team,
            "Speed":self.Speed,
            "Capacity":self.Capacity,
            "Crew_Size":self.Crew_Size,
            "Reliability_Rating":self.Reliability_Rating
        }





file_name="garage_data.json"

def save_data(garage):
    data = [car.to_dict() for car in garage]
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    garage = []
    if os.path.exists(file_name):
        try:
            with open (file_name, "r") as f:
                data=json.load(f)
                for item in data:
                    c_type = item.pop("type")
                    if c_type =="Racer":
                        garage.append(Racer(**item))
                    elif c_type =="SupportVehicle":
                        garage.append(SupportVehicle(**item))
        except Exception:
            pass
    return garage






garage = load_data()
while True:
    print("RADIATOR SPRINGS GARAGE MENU")
    print("1. Check In a Car")
    print("2. View Garage")
    print("3. Tune-Up")
    print("4. Retire a Car")
    print("5. Find a Car")
    print("6. Garage Report")
    print("7. Exit")
    choice = int(input(" Choose an Option (1-7) :"))

    if choice ==1:
        car_num = int(input("Enter Unique Car Number :"))
        for car in garage:
            if car.Car_Number == car_num: 
                print("Error:The Number already exists")
                continue
        name = input ("Enter Full Name :").strip()
        team = input ("Enter Racing Team :").strip()

        try:
            age=int(input("Enter Car's Age : "))
            speed=float(input("Enter Car's Speed:"))
            capacity=float(input("Enter Car's Capacity:"))

            car_type=int(input("Enter Car Type (1) Racer or (2) Support Vehicle:"))
            if car_type == 1:
                races=int(input(" Enter Races Completed : "))
                laps=float(input("Enter Laps Completed : "))
                new_car = Racer(car_num, name, age, team, speed, capacity, races, laps)
                garage.append(new_car)
                save_data(garage)
                print("Car checked in successfully")
            elif car_type == 2:
                crew=int(input(" Enter Crew Size : "))
                Reliability=float(input("Enter Reliability Rating : "))
                new_car = SupportVehicle(car_num, name, age, team, speed, capacity, crew, Reliability)
                garage.append(new_car)
                save_data(garage)
                print("Car checked in successfully")
            else:
                print("Invalid Error")
                continue
        except ValueError as e:
            print(f"Error:{e}")

        

    elif choice == 2:
        if not garage:
            print("Garage is empty")
        else: 
            print("Cars in garage : ")
            for car in garage:
                car.display()

    elif choice == 3:
        car_num = input("Enter Car Number to Tune-Up: ").strip()
        for car in garage:
            if car.Car_Number==car_num:
                try:
                    new_speed=float(input(f"Enter new speed (current speed:{car.Speed})<"))
                    if new_speed:
                        car.Speed=new_speed
                    new_capacity=float(input(f"Enter new capacity (current capacity:{car.Capacity})<ُEnter to skip>"))
                    if new_capacity:
                        car.Capacity=new_capacity
                    new_age=int(input(f"Enter new age (current age:{car.Age})"))
                    if new_age:
                        car.Age=new_age

                    if isinstance(car,Racer):
                        new_races_completed=int(input(f"Enter new number for races completed (current races completed:{car.Races_Completed})"))
                        if new_races_completed:
                            car.Races_Completed=new_races_completed
                        new_laps_completed=int(input(f"Enter new number for laps completed (current laps completed:{car.Laps_Completed})"))
                        if new_laps_completed:
                            car.Laps_Completed=new_laps_completed
                    elif isinstance(car,SupportVehicle):
                        new_crew_size=int(input(f"Enter new number for crew size (current crew size:{car.Crew_Size})"))
                        if new_crew_size:
                            car.Crew_Size=new_crew_size
                        new_reliability_rating=float(input(f"Enter new number for reliability rating (current reliability rating:{car.Reliability_Rating})"))
                        if new_reliability_rating:
                            car.Reliability_Rating=new_reliability_rating
                    save_data(garage)
                    print("Car details updated and saved successfully")
                except ValueError as e:
                    print(f"Input error:{e}")
                break
        else:
            print("Car not found")
    elif choice == 4:         
        car_num = int(input("Enter Car Number to be removed: "))
        for car in garage:
            if car.Car_Number==car_num:
                confirm = input(f"Are you sure you want to remove{car.Full_Name}[y/n] ").strip()
                if confirm =="y":
                    garage.remove(car)
                    save_data(garage)
                    print("Car removed successfully")
    elif choice == 5:
        car_num_or_name = input("Enter Car Number or Name you want to search about: ")
        for car in garage:
            if car.Full_Name==car_num_or_name:
                car.display()
            elif str(car.Car_Number)==car_num_or_name:
                car.display()
    elif choice == 6:
        if not garage:
            print("garage is empty")
        else:
            no_of_cars=len(garage)
            x=0;
            for car in garage:
                sum_performance_score=x+car.performance_score
                av_performance_score=sum_performance_score/no_of_cars
            teams={}
            for car in garage:
                teams[car.Racing_Team]=teams.get(car.Racing_Team,0)+1

            print("Garage Report")
            print(f"Total number of cars currently checked in:{no_of_cars}")
            print(f"Average performance score:{av_performance_score}")
            print(f"Cars per racing team:")
            for team_name,count in teams.items():
                print(f"{team_name}:{count}")
    elif choice == 7:
        print("Good bye")
        break
    else:
        print("Invalid choice")
        





            
            

        




                    





