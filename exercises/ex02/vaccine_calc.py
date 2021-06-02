"""Vaccine calculator."""

__author__ = "730314660"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


pop: str = input("What is the population? ")
adm: str = input("How many doses have been administered? ")
per_day: str = input("How many doses are administered per day? ")
target: str = input("What is the target for percent vaccinated? ")

int_pop = int(pop) 
int_adm = int(adm)
int_per_day = int(per_day)
int_target = int(target)
int_target_dec = (int_target) * .01 

days1: int = (int_target_dec) * (int_pop) * 2
days2: int = (days1) - (int_adm)
days3: int = round((days2) / (int_per_day))
str_days3 = str(days3)

today: datetime = datetime.today()
today.strftime("%B %d, %Y")
time_left: timedelta = timedelta(days3)
future: datetime = today + time_left
print(future)

print("Population: " + pop)
print("Doses administered: " + adm)
print("Doses per day: " + per_day)
print("Target percent vaccinated: " + target)
print("We will reach " + (target) + "% vaccination in " + (str_days3) + " days, which falls on " + (future.strftime("%B %d, %Y")))
