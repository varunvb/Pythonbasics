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
except IOError as err:
    print("The data file is missing: " + str(err))
    if  'data' in locals():
        data.close()
try:
    outfile1 = open("outputfile1", "w")
    outfile2 = open("outputfile2", "w")
    print(man, file=outfile1)
    print(other, file=outfile2)
except IOError:
    print("can't open files to write")
finally:
        outfile1.close()
        outfile2.close()
