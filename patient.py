def add_patient():
    with open("patient.txt", "a") as f:  #file in which details of patient will be stored
        patient_id = input("Enter Patient ID: ")
        name_p = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")
        gender = input("Enter Patient Gender: ")
        diagnosis = input("Enter Patient Diagnosis: ")
        
        # Write patient details to the file
        f.write(f"{patient_id},{name_p},{age},{gender},{diagnosis}\n")
        
    print("Patient is now registered with the hospital")
