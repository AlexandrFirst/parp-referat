from multiprocessing import Process, Lock, Value

# функція, що виконується у різних процесах
def process_fun(m_array, m_lock, array_sum):
    for elem in m_array:
        m_lock.acquire()  # захват замка
        array_sum.value = array_sum.value + elem
        m_lock.release() # визволенння замка

if __name__ == '__main__':
    # значення, що змінюється у процесах
    array_sum = Value('i', 0)

    # створення замка для синхронізації доступу до спільного ресурсу
    lock = Lock()
    procs = []
    arr = [1, 2, 3, 4, 5]
    for i in list(range(1, 4)):
        # створення нового процесу
        proc = Process(target=process_fun, args=(arr, lock, array_sum, ))
        procs.append(proc)
        proc.start()  # запуск створеного процесу
    for proc in procs:
        proc.join()  # очікування завершеня створених процесів
    print(array_sum.value)


