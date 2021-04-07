import MainFlight
import pytest


def test1_func():
    #t1 = travel("New York", "Beijing", 8000, 10, "ECONOMY")
    #t2 = travel("London", "New York", 6000, 6, "FIRST CLASS")
    #t3 = travel("Bengaluru", "Abu Dhabi", 3000, 3, "BUSINESS CLASS")
    pass


def test2_func():
    #p1 = PNR("24613", t1)
    pass


def test3_func():
    """To test the distance and the time taken"""
    assert MainFlight.distance_time[12] == (5600, 5)
    assert MainFlight.distance_time[34][0] == 2100

