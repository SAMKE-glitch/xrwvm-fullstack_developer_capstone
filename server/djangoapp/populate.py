from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description']
            )
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "mileage": 15000,
         "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "mileage": 20000,
         "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "mileage": 18000,
         "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "SUV", "year": 2023, "mileage": 12000,
         "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SUV", "year": 2023, "mileage": 10000,
         "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SUV", "year": 2023, "mileage": 13000,
         "car_make": car_make_instances[1]},
        {"name": "A4", "type": "SUV", "year": 2023, "mileage": 8000,
         "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year": 2023, "mileage": 9000,
         "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SUV", "year": 2023, "mileage": 9500,
         "car_make": car_make_instances[2]},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "mileage": 11000,
         "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year": 2023, "mileage": 14000,
         "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "mileage": 7000,
         "car_make": car_make_instances[3]},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "mileage": 7500,
         "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "Sedan", "year": 2023, "mileage": 8200,
         "car_make": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "mileage": 8800,
         "car_make": car_make_instances[4]},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            mileage=data['mileage']
        )
