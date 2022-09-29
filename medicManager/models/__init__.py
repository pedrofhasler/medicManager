from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = ((1, "Admin"), (2, "Medic"), (3, "Patient"))

from .Profile import Profile
from .DayWeek import DayWeek
from .Province import Province
from .City import City
from .Neighborhood import Neighborhood
from .Rating import Rating
from .Address import Address
from .Speciality import Speciality
