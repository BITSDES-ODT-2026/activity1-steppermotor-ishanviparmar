from machine import Pin
import time

l1 = Pin(15,Pin.OUT)
l2 = Pin(32,Pin.OUT)
l3 = Pin(19,Pin.OUT)
l4 = Pin(18,Pin.OUT)

x = [[1,0,0,0],[0,1,0,0], [0,0,1,0],[0,0,0,1]]
while True :
 for _ in range (0,500):
    
    for i in x:
        l1.value(i[0])
        l2.value(i[1])
        l3.value(i[2])
        l4.value(i[3])
        time.sleep(0.005)
        
 for k in range (500,1001):
    for i in reversed(x):
        l1.value(i[0])
        l2.value(i[1])
        l3.value(i[2])
        l4.value(i[3])
        time.sleep(0.005)
