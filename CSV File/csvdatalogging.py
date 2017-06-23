import csv
#import sys

"""f = open('/home/vikas/Downloads/feeds.csv', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        print row
finally:
    f.close()
"""
g= open('/home/vikas/Downloads/vikas.csv','wt')
writer=csv.writer(g)
for i in range(0,10):
 writer.writerow((i,i+10));
g.close();

