import csv
water = 0
with open("C:\Users\BSDU\Desktop\Operating System\database resources\zoo\zoo.csv") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    next(csv_reader)
    #to skip the header from csv file
    
    for row in csv_reader:
        if row[0] == "zebra":
          water=water + int(row[2]) 
          #print(row)
          print water


print 'elephant={}'.format(water)

print 'lion ={}'.format(water)
          
print 'taigar={}'.format(water)
for row in csv_reader:
    if row[0] =="zebra":
        water=water + int(row[2])
        #print(row)
        print
import csv
water = 0
water1 = 0
water2 = 0
water3 = 0
with poen ('zoo .csv') as csv_file:

     csv_reader = csv.reader(csv_file,delimiter=',')
     next(csv_reader)
     #to skip the header from csv file
     for row in csv_reader:
         #print (row)
         if row[0]not in animal_dictionary.keys:
             animal_dictionary[row]] = int(row[2])
         else:
             animal_dictionry[row[0]] = animal_dictionary[row[0]]+int(row[2])
print "all animals water needs are \n",animal_dictionary.items():
    print (key, valus)
         





        
for row in csv_reader.
if row[0]=='elephant':
    water=water +
