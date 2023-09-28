def convert_to_24_hour(hour, minute, period):
    # Check if the given period is "am"
    if period == "am":
        # Convert 12 AM to 0 hour in 24-hour format, otherwise keep the same hour
        if hour == 12:
            hour_24 = 0
        else:
            hour_24 = hour
            
    else:  # period == "pm"
        # Convert 12 PM to 12 hour in 24-hour format, otherwise add 12 to the hour
        if hour == 12:
            hour_24 = 12
        else:
            hour_24 = hour + 12
    
    # Format the 24-hour time in the format "HHMM"
    time_24_hour = "{:02d}{:02d}".format(hour_24, minute)
    
    # Return the converted 24-hour time
    return time_24_hour

print(convert_to_24_hour(8, 30, "am"))   # it returns "0830"
print(convert_to_24_hour(12, 0, "pm"))   # it returns  "1200"
print(convert_to_24_hour(1, 45, "pm"))   # it returns "1345"
print(convert_to_24_hour(11, 30, "am"))  # it returns  "1130"
print(convert_to_24_hour(6, 15, "pm"))   # it returns  "1815"