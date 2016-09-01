def what_is_the_time(time_in_mirror):
    # Constants
    DIFFERENCE = 12.0 * 60
    HOUR = 60
    TIME_LIST = time_in_mirror.split(":")

    # Calculating correct time
    delta = DIFFERENCE - (int(TIME_LIST[0]) * HOUR)
    if delta <= 60:
        delta += 12.0 * 60
        
    delta -= int(TIME_LIST[1])
    minutes = delta % HOUR
    hours = (delta - minutes) / HOUR

    # Outputting time
    if hours < 10:
        if minutes < 10:
            time = "0" + str(int(hours)) + ":" + "0" + str(int(minutes))
            return time
        time = "0" + str(int(hours)) + ":" + str(int(minutes))
        return time

    if minutes < 10:
        time = str(int(hours)) + ":" + "0" + str(int(minutes))
        return time
  
    time = str(int(hours)) + ":" + str(int(minutes))
    return time
        
# Testing
print what_is_the_time("06:35")
