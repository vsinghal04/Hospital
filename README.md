#here I have imported different modules 
#in which functions are there to perform the tasks
import patient 
import doctor
import appointment
import medicine
print('_______________________________________________')
print("WELCOME TO THE HOSPITAL MANAGEMENT SYSTEM")
print('_______________________________________________')
print('''Enter any key between 1 to 6 
      to manage the hospital management system.''')

doctors = []  # Initialized the doctors list

while True:  #menu driven program
    print("\n1.Enter the details of the new patient ")
    print("2.Enter the details of the new doctor joining the hospital ")
    print("3.Schedule appointment with the doctor ")
    print("4.MEDICINE STORE to buy medicine prescribed by the doctor")
    print("5.List of appointments.")
    print("6.Logging out of the hospital management system. ")
    choice = input("\nEnter your choice: ")
    if choice == '1':
        patient.add_patient()
    elif choice == '2':
        doctors = doctor.add_doctor(doctors)  # Pass the existing doctors list
    elif choice == '3':
        appointment.schedule_appointment()
    elif choice == '4':
        medicine.display_available_medicines()
        medicine_name = input("Enter the name of the medicine you want to buy: ")
        quantity = int(input("Enter the quantity you want to buy: "))
        medicine.buy_medicine(medicine_name, quantity)
    elif choice == '5':
        appointment.get_appointments()
    elif choice == '6':
        print('''Logging out
              Thank you for using this system.''')
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
#main file program ends here
