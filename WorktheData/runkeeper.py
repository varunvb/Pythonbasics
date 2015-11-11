from sanitizedata import sanitize


try:
    with open('julie.txt') as julierundata, open('james.txt')  as jamesrundata, open('mikey.txt') as mikeyrundata, open('sarah.txt') as sarahrundata:
        julie_run = julierundata.readline()
        julie_run = julie_run.strip().split(',')
        james_run = jamesrundata.readline()
        james_run = james_run.strip().split(',')
        mikey_run = mikeyrundata.readline()
        mikey_run = mikey_run.strip().split(',')
        sarah_run = sarahrundata.readline()
        sarah_run = sarah_run.strip().split(',')
except IOError as ioerr:
    print('File not found: ', str(ioerr))
clean_james = []
clean_mikey = []
clean_julie = []
clean_sarah = []
for each_string in julie_run:
    clean_julie.append(sanitize(each_string))
for each_string in james_run:
    clean_james.append(sanitize(each_string))
for each_string in mikey_run:
    clean_mikey.append(sanitize(each_string))
for each_string in sarah_run:
    clean_sarah.append(sanitize(each_string))
print(sorted(clean_julie))
print(sorted(clean_james))
print(sorted(clean_mikey))
print(sorted(clean_sarah))



