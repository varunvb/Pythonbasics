def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins+'.'+secs)

def load_coach_data (filename):
    try:
        with open(filename) as data:
            coach_data = data.readline()
            coach_data = coach_data.strip().split(',')
            (athlete_name, athlete_dob) = coach_data.pop(0), coach_data.pop(0)
            athlete_data = {'Name': athlete_name, 'Date-Of-Birth': athlete_dob, 'Times': coach_data }
            return (athlete_data)
    except IOError as ioerr:
        print('File cannot be open for reading: ', str(ioerr))
        return (None)
