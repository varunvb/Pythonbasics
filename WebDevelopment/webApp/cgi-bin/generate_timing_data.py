#!/usr/local/bin/python
import cgi
import athletemodel
import yate
import sys


athletes = athletemodel.get_from_store()
form_data = cgi.FieldStorage()
athlete_name = form_data["which_athlete"].value
print(yate.start_response())
print(yate.include_header('Coach Kellys Timing Data'))
print(yate.header("Athlete: " + athlete_name + "DOB: " + athletes[athlete_name].dob + "."))
print(yate.para("Top three times for this athlete are:"))
print(yate.u_list(athletes[athlete_name].top3()))
print(yate.include_footer({"Home":"/index.html", "Select another Athlete":"/cgi-bin/generate_list.py"}))