
import pywhatkit
import pandas

data = pandas.read_csv("students.csv")

for i in data.phone_number:
    pywhatkit.sendwhatmsg(i, "Geeks For Geeks!", 18, 30)