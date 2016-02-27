#id,surname,firstname,balance
from django.utils import timezone
from datetime import timedelta, datetime
import time

import random

import csv

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings

with open("data.csv") as f:
        print f
        reader = csv.reader(f)
        count = -1
        for row in reader:
            count += 1

            if count == 0:
                continue

            print "Creating record " + str(row)
            user = User.objects.create_user(
                username = str(row[1]) + str(row[2]) + str(count),
                first_name = row[2],
                last_name = row[1],
                password = "password"
            )

            _, created = Account.objects.get_or_create(
                user=user,
                balance = row[3]
                )
            # creates a tuple of the new object or
            # current object and a boolean of if it was created
