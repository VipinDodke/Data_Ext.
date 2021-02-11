import csv
d=[]
j=[]
minnum=9
mindata=''
maxnum = 1
maxdata = ''
with open('airlines.csv',newline='') as csvfile:
    spam = csv.reader(csvfile,quotechar='|')
    for row in spam:
        if row in d:
            j.append(row)
            continue
        d.append(row)

    for i in range (1,len(j)):
        y=1
        for p in range(1,len(j)):
            if (j[i]==j[p]):
                y=y+1
            if(minnum>y):
                minnum=y
                mindata=f'{j[i]}'
            if(maxnum<y):
                maxnum=y
                maxdata=f'{j[i]}'
print(minnum)
print(mindata)
print(maxnum)
print(maxdata)