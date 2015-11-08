from nester import print_lol
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
    with open('outfile1', 'w') as output1, open('outfile2', 'w') as output2:
        print_lol(man, indent=True, level=1, fh=output1)
        print_lol(other, indent=True, level=1, fh=output2)
except IOError as errout:
    print('FIles can\'t be written to' + str(errout))




