import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PurrfectPawPlacement.settings')
django.setup()

from Registration.models import ShelterGovernmentRecord # Update 'your_app_name' to the name of your Django app

def populate():
    shelters_data = [
        {"id": "A1B2C3D4E5F", "name": "Happy Tails Shelter", "email": "info@happytails.com", "address": "123 Bark St", "phoneNumber": "123-456-7890"},
        {"id": "G6H7I8J9K0L", "name": "Furry Friends", "email": "contact@furryfriends.org", "address": "456 Meow Ave", "phoneNumber": "098-765-4321"},
        {"id": "M1N2O3P4Q5R", "name": "Paws and Claws", "email": "hello@pawsclaws.net", "address": "789 Wag Way", "phoneNumber": "555-123-4567"},
        {"id": "S6T7U8V9W0X", "name": "Whisker Rescues", "email": "support@whiskerrescues.com", "address": "321 Purr Ln", "phoneNumber": "555-987-6543"},
        {"id": "Y1Z2A3B4C5D", "name": "Tail Waggers", "email": "tails@tailwaggers.org", "address": "654 Bark Park", "phoneNumber": "555-678-1234"},
        {"id": "E6F7G8H9I0J", "name": "The Cat's Meow", "email": "meow@catsmeow.net", "address": "987 Kitty Ct", "phoneNumber": "555-456-7890"},
        {"id": "K1L2M3N4O5P", "name": "Barking Lot", "email": "barks@barkinglot.com", "address": "123 Doggo Dr", "phoneNumber": "555-321-9876"},
        {"id": "Q6R7S8T9U0V", "name": "Feathered Friends", "email": "friends@feathered.org", "address": "456 Bird Blvd", "phoneNumber": "555-654-3210"},
        {"id": "W1X2Y3Z4A5B", "name": "Critter Care", "email": "care@critter.net", "address": "789 Squeak Sq", "phoneNumber": "555-567-8901"},
        {"id": "C6D7E8F9G0H", "name": "Four Paws", "email": "paws@fourpaws.org", "address": "321 Pawprint Pl", "phoneNumber": "555-890-1234"}
    ]
    
    for shelter in shelters_data:
        ShelterGovernmentRecord.objects.create(**shelter)

if __name__ == '__main__':
    print("Populating the ShelterGovernmentRecord model with 10 entries...")
    populate()
    print("Done.")
