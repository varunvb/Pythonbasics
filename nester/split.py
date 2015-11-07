import os
#os.chdir('/Users/varunvb')
data = open('/Users/varunvb/pythontestdelete')
for each_line in data:
    if not each_line.find(':') == -1:
        (roles, line_spoken) = each_line.split(':', 1)
        print (roles, end='')
        print (' said:')
        print(line_spoken, end='')
    else:
        print (each_line, end='')