import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Renames a Django project"

    def add_arguments(self, parser):
        parser.add_argument('new_proj_name', type=str, help="The new Django Project name")

    def handle(self, *args, **kwargs):
        new_proj_name = kwargs['new_proj_name']

        files_to_rename = ['django_boilerplate/settings/base.py', 'django_boilerplate/wsgi.py', 'manage.py']
        folder_to_rename = 'django_boilerplate'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('django_boilerplate', new_proj_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_proj_name)

        self.stdout.write(self.style.SUCCESS('Project name has been changed.'))
