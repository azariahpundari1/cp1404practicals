"""
CP1404 Programming II Practical 9
Silver Service Taxi tests
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

test = SilverServiceTaxi("Hammer", 200, 2)
print(test)
test.drive(18)
print(test)
test.start_fare()
print(test)
test.drive(100)
print(test)
test.start_fare()
print(test)