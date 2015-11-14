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
            #(athlete_name, athlete_dob) = coach_data.pop(0), coach_data.pop(0)
            return ({'Name': coach_data.pop(0), 'Date-Of-Birth': coach_data.pop(0), 'Times': str(sorted(set([sanitizedata.sanitize(time_string) for time_string in coach_data]))[0:3])})
    except IOError as ioerr:
        print('File cannot be open for reading: ', str(ioerr))
        return (None)
