def add_doctor(doctors):
    with open("doctor.txt", "a") as f:  # Open the file in append mode
    #it will not overwrite 
        doctor_id = input("Enter new Doctor ID: ")
        name_d = input("Enter Doctor Name: ")
        specialization = input("Enter doctor's specialization: ")
        
        # Write doctor details to the file
        f.write(f"{doctor_id},{name_d},{specialization}\n")
        
        # Append doctor details to the list
        doctors.append({
            'ID': doctor_id,
            'Name': name_d,
            'Specialization': specialization
        })
        
    print("Doctor is now registered with the hospital")
    return doctors

