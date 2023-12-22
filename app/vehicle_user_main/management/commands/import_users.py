from django.core.management.base import BaseCommand
from vehicle_user_main.models import Users
from csv import DictReader

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

class Command(BaseCommand):
    help = "A Command to add users csv file"


    def handle(self, *args, **options):
        if Users.objects.exists():
            print('User data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        print("Loading Users data")

        def clean_nan(value):
            return value if value.strip() != 'NaN' else None


        with open('users.csv') as file:
            reader = DictReader(file, delimiter='\t')
            field_names = reader.fieldnames[0].split()

        for row in DictReader(open('users.csv'), delimiter='\t'):
            cleaned_username = clean_nan(row['username'])
            cleaned_firstname = clean_nan(row['firstname'])
            cleaned_lastname = clean_nan(row['lastname'])

            if cleaned_username is not None and cleaned_firstname is not None and cleaned_lastname is not None:
                user = Users( username=cleaned_username, first_name=cleaned_firstname,
                            last_name=cleaned_lastname)
                user.save()

            else:
                print(f"Skipping entry with NaN values for username_id: {row['username']}")