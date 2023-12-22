from django.core.management.base import BaseCommand
from vehicle_user_main.models import Vehicle,Users
from csv import DictReader
import pandas as pd

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

class Command(BaseCommand):
    help = "A Command to add vehicle csv file"


    def handle(self, *args, **options):
        if Vehicle.objects.exists():
            print('vehicle data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        print("Loading Vehicle data")

        def clean_nan(value):
            return value if value.strip() != 'NaN' else None
        truck_number_user = {}

        # Read the CSV and get truck numbers
        for row in DictReader(open('vehicles.csv')):
            cleaned_truck_number = clean_nan(row['truck_number'])
            username = row['username']
            if cleaned_truck_number is not None:
                if cleaned_truck_number in truck_number_user:
                    truck_number_user[cleaned_truck_number] = username
                else:
                    truck_number_user[cleaned_truck_number] = username

        for truck_number, username in truck_number_user.items():
            user_obj, created = Users.objects.get_or_create(username=username)
            vehicle_obj, _ = Vehicle.objects.get_or_create(user=user_obj, truck_num=truck_number)


