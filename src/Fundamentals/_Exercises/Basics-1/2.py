#Write a Python program to display the 
# current date and time.
import datetime

now=datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d  %H:%M:%S")
print("Current date and time : " + formatted_date)