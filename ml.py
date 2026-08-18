import sqlite3
from sklearn import tree
import numpy as np

conn = sqlite3.connect('country.db')

cursor = conn.cursor()

cursor.execute("SELECT population, area FROM countries")

rows = cursor.fetchall()

data= []
for row in rows:
    data.append(row)
    

    
cursor.close()
conn.close()

x = []
y = []

for d in data:
    p = d[0]
    a = d[1]
    x.append([p])
    y.append(a)
    
x = np.array(x)
y = np.array(y)

clf = tree.DecisionTreeRegressor()
clf = clf.fit(x , y)

