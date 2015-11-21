import pickle
from sanitizedata import sanitize


class AthleteList:
    def __init__(self, ath_name, ath_dob=None, ath=[]):
        self.name = ath_name
        self.dob = ath_dob
        self.ath = ath
    def top3(self):
        return (sorted(set([sanitize (each_string) for each_string in self.ath]))[0:3])
def get_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
            return (AthleteList(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error' + str(ioerr))
        return (None)

def put_to_store (file_list):
    all_athletes = {}
    for each_file in file_list:
        ath = get_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_to_store): ' + str(ioerr))
    return (all_athletes)
def get_from_store ():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store): ' + str(ioerr))
    return (all_athletes)
the_files = ['james2.txt', 'julie2.txt', 'mikey2.txt', 'sarah2.txt']
data = put_to_store(the_files)
for each_athlete in data:
    print (data[each_athlete].name + "  " + data[each_athlete].dob)

data_copy = get_from_store()
for each_athlete in data_copy:
    print(data_copy[each_athlete].name + " " + data_copy[each_athlete].dob)






