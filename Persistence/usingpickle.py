from nester import print_lol
import pickle
man = []
other = []
try:
    with open('/Users/varunvb/pythontestdelete') as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken = line_spoken.strip()
                if role == 'Man':
                   man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError as err:
    print('Input file not found' + str(err))
try:
    with open('pickoutfile', 'wb') as pickfile1, open('pickother', 'wb') as pickfile2:
        pickle.dump(man, pickfile1)
        pickle.dump(other, pickfile2)
except pickle.PickleError as perr:
    print('FIles can\'t be written to' + str(perr))