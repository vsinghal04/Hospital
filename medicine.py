#medicine store of the hospital
medicines = {
    "Paracetamol": {"price": 10, "quantity": 50},
    "Aspirin": {"price": 15, "quantity": 30},
    "Antacid": {"price": 8, "quantity": 20},
    "DomDT": {"price": 20, "quantity": 20},
    "Moov Ointment": {"price": 10, "quantity": 10},
    "Sanitizer": {"price": 45, "quantity": 20},
    "Mask": {"price": 5, "quantity": 10},
    "Bandage": {"price": 5, "quantity": 20},
    "Emodium": {"price": 15, "quantity": 15}
    , "Electrol": {"price": 25, "quantity": 20}
    , "GluconD": {"price": 10, "quantity": 20}
    , "Normaxcin": {"price": 8, "quantity": 20}}
#function which will show all medicines available in the stock
def display_available_medicines():
    print("Available Medicines:")
    for name, details in medicines.items():
        print(f"{name}: Price - ${details['price']}, Quantity - {details['quantity']}")
#function to buy medicine
def buy_medicine(medicine_name, quantity):
    if medicine_name in medicines:
        if quantity <= medicines[medicine_name]["quantity"]:
            total_cost = quantity * medicines[medicine_name]["price"]
            print(f"You bought {quantity} {medicine_name}(s) for ${total_cost}.")
            medicines[medicine_name]["quantity"] -= quantity
        else:
            print(f"Sorry, only {medicines[medicine_name]['quantity']} {medicine_name}(s) available.")
    else:
        print("Medicine not found.")
