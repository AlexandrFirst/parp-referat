from multiprocessing import Process, current_process

def process_fun(array):
    # використання current_process() для отримання назви потоку
    # сумування масиву виконується функцією sum()
    print(f"{current_process().name} calculated sum: {sum(array)}")

if __name__ == '__main__':
    procs = []
    arr = [1, 2, 3, 4, 5]
    for i in list(range(1, 4)):
        proc = Process(target=process_fun, args=(arr,))  # створення нового процесу
        procs.append(proc)
        proc.start()  # запуск створеного процесу
    for proc in procs:
        proc.join()  # очікування завершеня створених процесів

