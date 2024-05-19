import time 
import threading

def calc_squares(num):
    print("calculate squares number /n")
    for n in num:
        print ('squares:',n*n ,'/n' )

def calc_cube (num):
    print("calculate cube number /n")
    for n in num:
        print ('cube:',n*n*n ,'/n' )

arr =[1,2,5,4]

t =time .time()
t1= threading.Thread(target=calc_squares, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print(threading._time)
print ("don   nothing ")
