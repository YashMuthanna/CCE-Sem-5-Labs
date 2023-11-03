class Owner:
    def __init__(self, name, address, profession, license_number):
        self.name = name
        self.address = address
        self.profession = profession
        self.license_number = license_number

    def displayOwner(self):
        print("Owner Details:")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Profession: {self.profession}")
        print(f"License Number: {self.license_number}")


class Car:
    def __init__(self, engine_number, registration_number, date_of_registration, color, owner, model):
        self.engine_number = engine_number
        self.registration_number = registration_number
        self.date_of_registration = date_of_registration
        self.color = color
        self.owner = owner
        self.model = model

    def displayCarDetails(self):
        print("Car Details:")
        print(f"Engine Number: {self.engine_number}")
        print(f"Registration Number: {self.registration_number}")
        print(f"Date of Registration: {self.date_of_registration}")
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")
        self.owner.displayOwner()


# Create an array of Owner objects
owners = [
    Owner("John Doe", "123 Main St", "Engineer", "AB123456"),
    Owner("Jane Smith", "456 Elm St", "Teacher", "CD789012"),
    Owner("Bob Johnson", "789 Oak St", "Doctor", "EF345678"),
    Owner("Alice Brown", "101 Pine St", "Artist", "GH901234"),
    Owner("Eve Wilson", "202 Cedar St", "Lawyer", "IJ567890")
]

# Create an array of Car objects
cars = [
    Car("123456", "ABC123", "2023-01-15", "Blue", owners[0], "Sedan"),
    Car("789012", "XYZ789", "2022-11-20", "Red", owners[1], "SUV"),
    Car("345678", "LMN456", "2021-09-05", "Green", owners[2], "Convertible"),
    Car("901234", "PQR789", "2023-03-10", "Black", owners[3], "Hatchback"),
    Car("567890", "UVW123", "2020-12-30", "Silver", owners[4], "SUV")
]

# Display details of all cars along with their owners
for i, car in enumerate(cars, 1):
    print(f"\nCar {i} Details:")
    car.displayCarDetails()
