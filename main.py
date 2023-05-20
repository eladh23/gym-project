from members import GymMembersList
from machine import MachineList
from subscription import SubscriptionList 

membership_list = GymMembersList()
membership_list.load_to_file("member.json")
machine_list = MachineList()
machine_list.load_to_file("machine.json")      
subscription_list = SubscriptionList()
subscription_list.load_to_file("subs.json")

while True:
      print("Wellcome ,'Python Power Fitness'.")
      print("Enter a choice: ")
      print("1. Add member.")
      print("2. Remove member.")
      print("3. Show members.")
      print("4. Update member.")
      print("5. Add machine.")
      print("6. Remove machine.")
      print("7. Show machines.")
      print("8. Update machine.")
      print("9. Add new subscription.")
      print("10. Remove subscription.")
      print("11. Show all subscriptions.")
      print("12. Show the end date.")
      print("13. Show days left by member ID.")
      print("0. Exit.")
      choice = input("Enter your choice: ")
      if choice == "1":
            membership_list.add_member()
      elif choice == "2":
            membership_list.remove_member()      
      elif choice == "3":
            membership_list.show_all_members()
      elif choice == "4":
            membership_list.update_member()
      elif choice == "5":
            machine_list.add_machine()
      elif choice == "6":
            machine_list.remove_machine()
      elif choice == "7":
            machine_list.show_all_machines()
      elif choice == "8":
            machine_list.update_machine()
      elif choice == "9":
            subscription_list.add_subscription() 
      elif choice == '10':
            subscription_list.delete_subscription()
      elif choice == "11":
            subscription_list.show_all_subs()
      elif choice == "12":
            subscription_list.get_end_date()
      elif choice == "13":
            subscription_list.get_days_left()
      elif choice == '0':
            print("Thank you for using our GYM MENU .'Python Power Fitness', Goodbye!")
            break
      else: print("Invalid choice, please try again.")
      

      
