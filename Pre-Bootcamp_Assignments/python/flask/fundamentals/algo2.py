
# - Create a function clockHandAngles(seconds) that given the number of seconds since 12:00:00, will print the angles in degress of the hour, minute and second hands.
#         there are 360 degress in a full arc rotation. Treat "straight up" 12:00:00 as 0 degress for all hands


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# - write a function given a 12 hour AM/PM format, ('01:01:00PM), returns time converted to military time, (13:01:00)
#     - example timeconvert('01:45:00PM') returns '13:45:00'
#     - example 2 timeconvert('12:59:00AM') returns '00:59:00'

def time_convert(time):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[2:-2]
    # remove the AM    
    elif time[-2:] == "AM":
        return time[:-2]
    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif time[-2:] == "PM" and time[:2] == "12":
        return time[:-2]
    else:
        # add 12 to hours and remove PM
        return str(int(time[:2]) + 12) + time[2:8]

print(time_convert('01:45:00PM'))
print(time_convert('12:59:00AM'))
print(time_convert('10:00:00AM'))

# ---------------------------------------------------------------------------

def time_convert(time):
    if 'AM' in time.upper():
        if '12' in time:
            return "00" + time[2:-2]
        else:
            return time[:-2]
    elif 'PM' in time.upper():
        if '12' in time:
            return time[2:-2]
        else:
            return str(int(time[:2])+12) + time[2:-2]

print(time_convert('01:45:00 PM   '))
print(time_convert('12:59:00 am'))
print(time_convert('10:00:00 am'))

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def timeconvert(time):
    hour = "00"
    if time[len(time.strip())-2:] == "PM":
        if time.strip()[:2] == "12":
            hour = "12"
        else:
            hour = int(time.strip()[:2]) + 12
    else:
        if time[:2] != "12":
            hour = time.strip()[:2]
    return f'{hour}{time.strip()[2:len(time.strip())-2]}'

print(timeconvert('01:45:00 PM '))
print(timeconvert('12:59:00 am     '))
print(timeconvert('10:00:00 am                       '))