from sanitizedata import sanitize


class Athlete:
    def __init__(self, a_name, a_dob, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return (sorted(set([sanitize(each_string) for each_string in self.times]))[0:3])
def get_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
            return (Athlete(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error', str(ioerr))
        return (None)
james = get_data('julie2.txt')
print(james.name +' top 3 speeds are: ' + str(james.top3()))

