man = []
other = []
try:
    data = open('/Users/varunvb/pythontestdelete')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append (line_spoken)
        except ValueError:
            pass
    data.close()

except IOError:
    print("The data file is missing")
try:
    outfile1 = open("outputfile1", "w")
    outfile2 = open("outputfile2", "w")
    print(man, file=outfile1)
    print(other, file=outfile2)
    outfile1.close()
    outfile2.close()
except IOError:
    print("can't open files to write")
