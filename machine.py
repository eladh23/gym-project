from enum import Enum
import json

class Machine:
        
    def __init__(self, name, machine_id, difficulty_level, muscles_group):
        self.name = name
        self.machine_id = machine_id
        self.difficulty_level = difficulty_level
        self.muscles_group = muscles_group

    def __str__(self):
        return f"Name: {self.name}, Machine ID: {self.machine_id}, Difficulty Level: {self.difficulty_level}, Muscles Group: {self.muscles_group}"

     
class MachineList:
    def __init__(self):
        self.machines = []
        
    def add_machine(self):
        name = input("Enter machine name: ")
        machine_id = int(input("Enter machine ID: "))
        while True : 
            if any(machine.machine_id == machine_id for machine in self.machines):
                print("error: there is a machine with the same ID.")
                machine_id = int(input("Enter machine ID: "))
            else :
                break        
        difficulty_level = (input("Enter difficulty_level : "))       
        muscles_group = input("Enter muscles_group of the machine: ")
        self.machines.append(Machine(name, machine_id, difficulty_level, muscles_group))
        self.save_machines_to_file("machine.json")
        print(f"Added machine {name} with ID {machine_id} to the list.")
    
    def remove_machine(self):
        machine_id = int(input("Enter machine ID you want to remove:"))
        found = False
        for machine in self.machines:
            if machine.machine_id == machine_id:
                self.machines.remove(machine)
                self.save_machines_to_file("machine.json")
                print("Machine remove successfuly ")
                found = True
                break
        if not found:
            print(f"Machine with ID number {machine_id} not found.")    
    
    def show_all_machines(self):
        with open("machine.json", "r") as f:
            data = json.load(f)
        if not data:
            print("No machines in the list.")
        else:
            for machine_data in data:
                machine = Machine(machine_data["name"], machine_data["machine_id"], machine_data["difficulty_level"], machine_data["muscles_group"])
                print(f"Name: {machine.name}, Machine ID: {machine.machine_id}, difficulty is {machine.difficulty_level}, Worked on {machine.muscles_group}")
    

    def update_machine(self):
        machine_id = int(input("Enter machine ID to update: "))
        found = False
        for machine in self.machines :
                if machine.machine_id == machine_id:
                    found = True
                    break
        if not found :
                print(f"there is no machine with ID : {machine_id}")
                return 
        name = input("Enter new machine name (leave blank to keep current): ")
        difficulty_level = input("Enter new difficulty level (leave blank to keep current): ")
        muscles_group = input("Enter new muscles group (leave blank to keep current): ")
    
        with open('machine.json', 'r') as f:
            machines = json.load(f)
        
        for machine in machines:
            if machine['machine_id'] == machine_id :
                if name:
                    machine['name'] = name
                    
                if difficulty_level:
                    machine['difficulty_level'] = difficulty_level
                    
                if muscles_group:
                    machine['muscles_group'] = muscles_group
        
        with open('machine.json', 'w') as f:
            json.dump(machines, f)
        print(f"Updated machine with ID {machine_id} in the file.")

    def save_machines_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([machine.__dict__ for machine in self.machines], f, indent=4)
        print(f"Saved {len(self.machines)} machines to file {filename}.")
        
    def load_to_file(self ,fillename):
        with open(fillename) as f:
            all_file_json = json.load(f)
        for single_json in all_file_json:
            machine = Machine(**single_json)
            self.machines.append(machine)