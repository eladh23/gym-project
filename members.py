from enum import Enum
import json

class GymMember:
    class Ages(Enum):
        MINIMUM_AGE = 16
        MAXIMUM_AGE = 67
    def __init__(self, name, member_id, age, city):
        self.name = name
        self.member_id = member_id
        self.age = age
        self.city = city

    def __str__(self):
        return f"the name is {self.name} his ID-number :{self.member_id} ,{self.age} year old, lives in {self.city}"


class GymMembersList:
    
    def __init__(self):
        self.members = []

    def add_member(self) : 
        name = input("Enter member name: ")
        member_id = int(input("Enter member ID: "))
        while True: 
            if any(member.member_id == member_id for member in self.members):
                print("This ID already exists. Please enter a different ID.")
                member_id = int(input("Enter member ID: "))
            else:
                break
        while True:
            age = int(input("Enter member age (between 16 and 67): "))
            if GymMember.Ages.MINIMUM_AGE.value <= age and age <= GymMember.Ages.MAXIMUM_AGE.value :
                break
            else:
                print("Invalid age! Please enter an age between 16 and 67.")
        city = input("Enter member city: ")
        self.members.append(GymMember(name, member_id, age, city))
        self.save_members_to_file("member.json")
        
    def remove_member(self):
        member_id = int(input("Enter member ID you want to remove:"))
        found = False
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                self.save_members_to_file("member.json")
                print("member removed successfully.")
                found = True
                break
        if not found:
            print(f"member with name {member_id} not found.")

    def show_all_members(self):
        with open("member.json", "r") as f:
            data = json.load(f)
        if not data:
            print("No machines in the list.")
        else:
            for member_data in data:
                member = GymMember(member_data["name"], member_data["member_id"],member_data["age"], member_data["city"])
                print (f"Name: {member.name}, Member ID: {member.member_id}, Age: {member.age}, City: {member.city}")

    def update_member(self):
        member_id = int(input("Enter member ID to update: "))
        found = False
        for member in self.members:
            if member.member_id == member_id:
                found = True
                
                while True:
                    age_input = input("Enter member age (between 16 and 67): ")
                    if age_input == '':
                        age = member.age
                        break
                    else:
                        age = int(age_input)
                        if GymMember.Ages.MINIMUM_AGE.value <= age <= GymMember.Ages.MAXIMUM_AGE.value:
                            break
                        else:
                            print("=========================================================")
                            print("===Invalid age! Please enter an age between 16 and 67.===")
                            print("=========================================================")

                name = input("Enter new member name (leave blank to keep current): ")
                city = input("Enter new member city (leave blank to keep current): ")
                with open('member.json', 'r') as f:
                    members = json.load(f)
                for member in members:
                    if member['member_id'] == member_id:
                        if name:
                            member['name'] = name
                        if age:
                            member['age'] = age
                        if city:
                            member['city'] = city
                            
                with open('member.json', 'w') as f:
                    json.dump(members, f)
                print(f"Updated member with ID {member_id} in the file.")
        if not found:
            print(f"Member with ID number {member_id} not found.")

    def save_members_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([member.__dict__ for member in self.members], f)
        print(f"Saved {len(self.members)} members to file {filename}.")

    def load_to_file(self, fillename):
        with open(fillename) as f:
            all_file_jsons = json.load(f)
            for single_json in all_file_jsons:
                member = GymMember(**single_json)
                self.members.append(member)