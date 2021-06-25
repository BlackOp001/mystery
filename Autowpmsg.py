import pywhatkit
number=input("number you want to msg:")
message=str(input("your msg:"))
hour=int(input("hour:"))
minutes=int(input("minutes:"))
pywhatkit.sendwhatmsg(number ,message,hour,minutes)
