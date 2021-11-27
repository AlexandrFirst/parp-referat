import threading
import time

def thread_func(sleep_time):  # функція що виконується паралельно
    time.sleep(0.01)
    print("Executing long-running task")
    time.sleep(sleep_time)  # емуляція виконання довгої задачі

if __name__ == '__main__':
    thread = threading.Thread(target=thread_func, args=(2,))  # створення потоку
    thread.start()  # запуск потоку
    print("Waiting for thread to end")
    thread.join()  # очікування завершування потоку
    print("Thread is over")
