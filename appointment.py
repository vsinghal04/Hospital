appointments = []  # Initialize the empty appointments list

def schedule_appointment():
    patient_id = input("Enter Patient ID: ")
    doctor_id = input('Enter doctor ID: ')
    appointment_date = input('Enter the date (YYYY-MM-DD) ')
    
    # Create a dictionary for the appointment details
    appointment = {"patient_id": patient_id, "doctor_id": doctor_id, "appointment_date": appointment_date}
    
    # Append the appointment to the appointments list
    appointments.append(appointment)

def get_appointments():
    print(appointments)
#it will print the list of oppointment which user asks