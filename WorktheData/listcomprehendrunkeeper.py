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
print (sorted([sanitize(each_string) for each_string in julie]))
print (sorted([sanitize(each_string) for each_string in mike]))
print (sorted ([sanitize(each_string) for each_string in sarah]))
print (sorted ([sanitize(each_string) for each_string in james]))


