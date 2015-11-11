from sanitizedata import sanitize


def read_files(each_file):
    try:
        with open(each_file) as data:
            speeds = data.readline()
            return (speeds.strip().split(','))
    except IOError as ioerr:
        print('Can\'t open file for reading: ', str(ioerr))

james = read_files('james.txt')
mikey = read_files('mikey.txt')
sarah = read_files('sarah.txt')
julie = read_files('julie.txt')
print (sorted(set([sanitize(each_t) for each_t in james]))[0:3])
print (sorted(set([sanitize(each_t) for each_t in julie]))[0:3])
print (sorted(set([sanitize(each_t) for each_t in sarah]))[0:3])
print (sorted(set([sanitize(each_t) for each_t in mikey]))[0:3])
