import csv

"""g=open("/home/vikas/Desktop/file.csv",'wt');

writer=csv.writer(g);

for i in range(1,21):
 writer.writerow((i,i*10));
g.close();
"""

f=open('/home/vikas/Desktop/file.csv','rt');
reader=csv.reader(f);

for row in reader:
 print row;

f.close();

