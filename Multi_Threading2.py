import multiprocessing


def square_list (myList,q):
    for number in myList:
        q.put(number*number)

def print_queue (q):
    print ("queue elements")
    while not q.empty():
        print(q.get ())
    print("queue is empty")


if __name__ == "__main__":
    myList =[1,2,3,4]

    q=multiprocessing.Queue()

    p1 =multiprocessing.Process(target=square_list, args=(myList,q))
    p2 =multiprocessing.Process(target=print_queue, args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()


