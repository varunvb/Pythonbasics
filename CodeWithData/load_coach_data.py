from sanitizedata import sanitize
from sanitizedata import load_coach_data

lc_james = load_coach_data('james2.txt')
lc_julie = load_coach_data('julie2.txt')
print(lc_james['Name'] + " fastest times are: " + str(sorted(set(lc_james['Times']))[0:3]))
print(lc_julie['Name'] + ' fastest times are: ' + str(sorted(set(lc_julie['Times']))[0:3]))







