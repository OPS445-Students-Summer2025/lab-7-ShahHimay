#!/usr/bin/env python3
# Student ID: 118541234
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        if not all(isinstance(i, int) for i in [hour, minute, second]):
            raise TypeError("Hour, minute, and second must be integers")
        self.hour = hour
        self.minute = minute
        self.second = second

def sum_times(t1, t2):
    """Add two time objects and return the sum with carryover."""
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second = sum.second % 60

    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute = sum.minute % 60

    return sum

def format_time(t):
    """Return time in HH:MM:SS format."""
    return f"{t.hour:02}:{t.minute:02}:{t.second:02}"
