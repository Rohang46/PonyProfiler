import numpy as np
import time
#import CNNModel 
import sqlite3 
from keras.models import load_model
a=1
b=0.33
c=1
d=0.33
e=1
f=30
g=0
h=1
i=35
j=448
k=604

model = load_model('model1.h5')
predicted = model.predict(a,b,c,d,e,f,g,h,i,j,k)
print(predicted)
