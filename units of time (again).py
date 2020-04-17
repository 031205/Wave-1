totalseconds = int(input('Input the number of seconds:'))
days = totalseconds//86400
hours = (totalseconds%86400)//3600
minutes = (totalseconds%3600)//60
seconds = totalseconds%60
print(days,':',hours,':',minutes,':',seconds,sep='')