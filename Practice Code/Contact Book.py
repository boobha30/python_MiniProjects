
contact = {}
while True:
    name=input("Enter the contact name: ")
    phone_number=input("Enter the contact phone number with country code (eg.+65 xxxxxxxx): ")
    if not phone_number.startswith('+'):
        print("Invalid phone number format. Please include the country code starting with '+'.")
        continue
    contact[name]=phone_number
    add_another=input("do you want to add another contact? (yes/no): ")
    if add_another.lower() != "yes":
        break
print("Contact added successfully!")
print("Current contact book:")
for name, phone_number in contact.items():
    print(f"{name}: {phone_number}")