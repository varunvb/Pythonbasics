from sanitizedata import sanitize


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return (sorted(set([sanitize(each_string) for each_string in self.times]))[0:3])
    def add_times ()

    def add_time(self, ad_time):
        self.times.append(ad_time)
    def add_times(self, ad_times=[]):
        self.times.extend(ad_times)

def get_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
            return (Athlete(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error' + str(ioerr))
        return (None)
sarah = get_data('sarah2.txt')
james = get_data('james2.txt')
mikey = get_data('mikey2.txt')
julie = get_data('julie2.txt')
james.add_time('2.00')
vera = Athlete('Vera Vi', '')
vera.add_times(['2.30', '2.10', '2.40', '2.30'])
print(vera.top3())
mikey.add_times(['2.20', '2.00', '2.10'])
print(sarah.name +'\'s top 3 speeds are: ' + str(sarah.top()))
print(james.name + '\'s fastest times are: ' + str(james.top3()))
print(mikey.name + '\'s fastest times are: ' + str(mikey.top3()))
print(julie.name + '\'s fastest times are: ' + str(julie.top3()))