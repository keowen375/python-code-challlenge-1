"""
    Challenge 1: Converting 12-hour time to 24-hour time

    Converting a 12-hour time like "8:30 am" or "8:30 pm" 
    to 24-hour time (like "0830" or "2030") sounds easy enough, 
    right? Well, let's see if you can do it!

    You will have to define a function, which will be given an hour 
    (always in the range of 1 to 12, inclusive), a minute (always 
    in the range of 0 to 59, inclusive), and a period (either "am" 
    or "pm") as input.

    Your task is to return a four-digit string that encodes that 
    time in 24-hour time.

    Notes:
    By convention, noon is 12:00 pm, and midnight is 12:00 am.

    On 12-hours clock, there is no 0 hour, and time just after midnight 
    is denoted as, for example, 12:15 am. On 24-hour clock, this translates 
    to 0015. 
"""


def convert_12_hour_time_to_24_hour_time(hour, minute, preriod):
    if minute < 10:
        minute = f"0{str(minute)}"

    if preriod == "am":
        if hour < 10:
            hour = f"0{str(hour)}"
        time = f"{str(hour)}{str(minute)}"
        return time
    else:
        if hour == 12:
            hour = "00"
        else:
            hour = hour + 12
        time = f"{str(hour)}{minute}"
        return time
