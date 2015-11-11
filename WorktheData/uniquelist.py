from sanitizedata import sanitize


try:
    with open ('julie.txt') as juldata, open('james.txt') as jamedata, open('sarah.txt') as saradata, open('mikey.txt') as mikedata:
        julie = juldata.readline()
        julie = julie.strip().split(',')
        mike = mikedata.readline()
        mike = mike.strip().split(',')
        sarah = saradata.readline()
        sarah = sarah.strip().split(',')
        james = jamedata.readline()
        james = james.strip().split(',')
except IOError as ioerr:
    print ('can\'t open files for reading: ', str(ioerr))
julie = (sorted([sanitize(each_string) for each_string in julie]))
mike =  (sorted([sanitize(each_string) for each_string in mike]))
sarah = (sorted ([sanitize(each_string) for each_string in sarah]))
james = (sorted ([sanitize(each_string) for each_string in james]))
unique_julie  = []
unique_sarah = []
unique_james = []
unique_mike = []
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
    if each_t not in unique_james:
        unique_james.append(each_t)
    if each_t not in unique_mike:
        unique_mike.append(each_t)
print(unique_mike[0:3])
print(unique_sarah[0:3])
print(unique_james[0:3])
print(unique_julie[0:3])

