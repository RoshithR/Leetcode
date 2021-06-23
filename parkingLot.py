
from enum import Enum
class VehicleType(Enum):
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1,2,3,4,5

class ParkingSpotType(Enum):
    HANDICAPPED, LARGE, COMPACT, MOTORBIKE, ELECTRIC = 1,2,3,4,5

class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1,2,3,4,5,6

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

class Person:
    def __init__(self, name, address, email, phone):
        self.name = name
        self.address=address
        self.email=email
        self.phone=phone


