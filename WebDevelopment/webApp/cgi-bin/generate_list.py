#!/usr/local/bin/python
import athletemodel
import yate
import glob


data_files = glob.glob("/Users/varunvb/PycharmProjects/LearnPython/WebDevelopment/webApp/data/*.txt")
athletes = athletemodel.put_to_store(data_files)
print(yate.start_response())
print(yate.include_header('Coach Kelly\'s List of Athletes'))
print(yate.start_form('generate_timing_data.py'))
print(yate.para('select an athlete from the list to work with:'))
for each_ath in athletes:
    print(yate.radio_button( 'Which Athlete?', athletes[each_ath].name))
print(yate.end_form('select'))
print(yate.include_footer({'Home': "/index.html"}))
