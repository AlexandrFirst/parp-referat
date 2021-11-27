import multiprocessing
from multiprocessing import Pool, Pipe


def pipe_sender(infos, pipe_con, queue):
    send_message_count = 0
    for info in infos:
        # отримання повідомлення про дозвіл відправити дані
        queue_msg = queue.get()
        print(f"Pipe sender sends: {info}")
        pipe_con.send(info)  # відправка даних
        send_message_count = send_message_count + 1
    return send_message_count


def pipe_reciever(pipe_conn, queue):
    recieved_message_count = 0
    while True:
        queue.put("msg")  # повідомлення іншого процесу,
                          # про готовність отримувати дані

        info = pipe_conn.recv()  # отримання даних

        # підрахунок отриманих даних
        recieved_message_count = recieved_message_count + 1
        if info == 'end':
            break
        print(f"Reciever gets: {info}")
    print("No more information from other pipe")
    return recieved_message_count


if __name__ == "__main__":
    # створення інформвції, що передається у процеси
    info_arr = ["This", "are", "messages", "end"]
    m = multiprocessing.Manager()
    q = m.Queue()  # створення Queue
    pipe_conn1, pipe_conn2 = Pipe() # створення Pipe

    # створення пула процесів з двама активними робітниками
    pool = Pool(processes=2)
    # відправка задач у пул процесів
    sent_messages = pool.apply_async(pipe_sender, args=(info_arr, pipe_conn1, q, ))
    recieved_message = pool.apply_async(pipe_reciever, args=(pipe_conn2, q, ))
    # завершення роботи пулу процесів
    pool.close()
    pool.join()
    # виведення результатів роботи пулу
    print(f"Send messages count: {sent_messages.get()}")
    print(f"Recieved messages count: {recieved_message.get()}")


