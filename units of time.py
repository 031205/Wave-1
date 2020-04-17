days = int(input('Input the number of days:'))
hours = int(input('Input the number of hours:'))
minutes = int(input('Input the number of minutes:'))
seconds = int(input('Input the number of seconds:'))
totalseconds = days*86400 + hours*3600 + minutes*60 + seconds
print('The total number of seconds is',totalseconds)