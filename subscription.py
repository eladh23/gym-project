from datetime import datetime ,timedelta
from enum import Enum
import json

class Subs:
    class SubscriptionType(Enum):
        YEAR = 'year'
        MONTH = 'month'
        WEEK = 'week'

    def __init__(self, member_id, subscription_type, start_date):
        self.member_id = (member_id)
        self.subscription_type = subscription_type
        if isinstance(start_date, str):
            self.start_date = datetime.strptime(start_date, '%Y-%m-%d').date().isoformat()
        else:
            self.start_date = start_date.isoformat()
            
    def __str__(self):
        return f'Subscriber ID: {self.member_id}\nSubscription Type: {self.subscription_type.name}\nStart Date: {self.start_date.strftime("%Y-%m-%d")}\n'


class SubscriptionList:
    def __init__(self):
        self.subscriptions = []

    def add_subscription(self):
        member_id = int(input("Enter member ID: "))
        while True: 
            if any (sub.member_id == member_id for sub in  self.subscriptions):
                print("error: there is a member with the same ID.")
                member_id = int(input("Enter member ID: "))
            else :
                break    
        subscription_type = input("Enter subscription type (Year/Month/Week): ")
        
        while True:
            start_date_str = input("Enter start date (YYYY-MM-DD): ")
            try:
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
                break
            except ValueError:
                print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")
        self.subscriptions.append(Subs(member_id, subscription_type, start_date))
        self.save_subscription_to_file("subs.json")
        print(f"Added member with ID {member_id} to the list.")

    def delete_subscription(self):
        member_id = int(input("Enter member ID you want to remove:"))
        found = False
        for subscriber in self.subscriptions :
            if subscriber.member_id == member_id:
                self.subscriptions.remove(subscriber)
                self.save_subscription_to_file("subs.json")
                print("Subscriber remove successfuly ")
                found = True
                break
        if not found:
            print(f"subscriber with ID {member_id} not found.")

    def show_all_subs(self):
        with open("subs.json", "r") as f:
            data = json.load(f)
        if not data:
            print("No subscribers in the list.")
        else:
            for subscriber_data in data:
                subscriber = Subs(subscriber_data["member_id"], subscriber_data["subscription_type"], subscriber_data["start_date"])
                self.subscriptions.append(subscriber)
                print(f"member_id :{subscriber.member_id}, subscription_type {subscriber.subscription_type}, start_date :{subscriber.start_date}")

    def get_end_date(self):
        member_id_search = int(input("Enter subscriber ID: "))
        for subscriber in self.subscriptions:
                if subscriber.member_id == member_id_search : 
                    if subscriber.subscription_type == Subs.SubscriptionType.YEAR.value:
                        start_date = datetime.strptime(subscriber.start_date, '%Y-%m-%d')  
                        end_date = start_date + timedelta(days=365)
                        print(f"end day : {end_date.isoformat()}") 
        
                    elif subscriber.subscription_type == Subs.SubscriptionType.MONTH.value:
                        start_date = datetime.strptime(subscriber.start_date, '%Y-%m-%d')  
                        end_date = start_date + timedelta(days=30)
                        print(f"end day : {end_date.isoformat()}") 

                    elif subscriber.subscription_type == Subs.SubscriptionType.WEEK.value:
                        start_date = datetime.strptime(subscriber.start_date, '%Y-%m-%d')  
                        end_date = start_date + timedelta(days=7)
                        print(f"end day : {end_date.isoformat()}")
                    else :
                        print(f"There is no member with ID {member_id_search}.")    
                        
            
    def get_days_left(self):
        member_id_search = int(input("Enter subscriber ID: "))
        for subscription in self.subscriptions:
            if subscription.member_id == member_id_search:
                start_date = datetime.strptime(subscription.start_date, '%Y-%m-%d') 
                if subscription.subscription_type == "year":
                    end_date = start_date + timedelta(days=365)
                elif subscription.subscription_type == "month":
                    end_date = start_date + timedelta(days=365)
                elif subscription.subscription_type == "week":
                    end_date = start_date + timedelta(days=365)
                else :
                    print(f"Subscriber not found with {member_id_search} ID ")
                          
                days_left = (end_date - datetime.now()).days
                print(f"The Subscriber with ID : {member_id_search} has {days_left}")
                
    def save_subscription_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump([subscription.__dict__ for subscription in self.subscriptions], f)
        print(f"Saved {len(self.subscriptions)} subscriptions to file {filename}.")

    def load_to_file(self, fillename):
        with open(fillename) as f:
            all_file_json = json.load(f)
        for single_json in all_file_json:
            sub = Subs(**single_json)
            self.subscriptions.append(sub)





