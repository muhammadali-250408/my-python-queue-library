from queue import Queue

max_size_inp: int = input(">> MAX QUEUE SIZE: ")
queue = Queue(max_size_inp)

while True:
    user_inp = input(">> SELECT AN OPTION:\n    >> ENQUEUE [A]\n    >> DEQUEUE [B]\n    >> ISEMPTY [C]\n    >> ISFULL [D]\n    >> EXIT [E]\n>> INPUT: ")
    user_inp = user_inp.upper()

    if user_inp == "A":
        val = input(">> VALUE: ")
        queue.enQueue(val)
        print(queue.queue)

    elif user_inp == "B":
        val = queue.deQueue()
        print(val)

    elif user_inp == "C":
        val = queue.isEmpty()
        if val:
            print("QUEUE IS EMPTY")
        else:
            print("QUEUE IS NOT EMPTY")

    elif user_inp == "D":
        val = queue.isFull()
        if val:
            print("QUEUE IS FULL")
        else:
            print("QUEUE IS NOT FULL")

    else:
        quit()
