#﻿ id,surname,firstname,balance

from django.utils import timezone
from datetime import timedelta, datetime
import time

import random

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rango_project.settings')

import django
django.setup()

from rango.models import *
from django_messages.models import *
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings

with open("data.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Teacher.objects.get_or_create(
                first_name=row[0],
                last_name=row[1],
                middle_name=row[2],
                )
            # creates a tuple of the new object or
            # current object and a boolean of if it was created
