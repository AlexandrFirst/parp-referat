from random import randint
from multiprocessing import Pool
import time


result = [[]]


def create_matrix(n, m):
    return [[randint(-1000, 1000) for i in range(m)] for i in range(n)]


def multiply_matrix(m1, m2):
    global result  # глобальний масив у якому збурігається результат
    result = [[0 for i in range(0, len(m2[0]))] for i in range(0, len(m1))]
    start = time.time()
    for index_i in range(0, len(m1)):
        for index_j in range(0, len(m2[0])):
            temp_sum = 0
            for index_k in range(0, len(m2)):
                temp_sum = m1[index_i][index_k] + m2[index_k][index_j]
            result[index_i][index_j] = temp_sum
    end = time.time()
    print(f"Elapsed time for sync function: {end - start}")


def row_column_sum(index_i, m1, m2):
    row_to_return = []
    for index_j in range(0, len(m2[0])):
        temp_sum = 0
        for index_k in range(0, len(m2)):
            temp_sum = m1[index_i][index_k] + m2[index_k][index_j]
        row_to_return.append(temp_sum)
    return row_to_return, index_i


def row_column_sum_callback(call_back_result):
    global result  # глобальний масив у якому зберыгаэться результат множення
    result[call_back_result[1]] = call_back_result[0]


def multiply_matrix_async(m1, m2):
    global result
    pool = Pool(processes=4)
    pool_results = []
    for index_i in range(0, len(m1)):
        sum_result = pool.apply_async(row_column_sum, args=(index_i, m1, m2,), callback=row_column_sum_callback)
        pool_results.append(sum_result)

    start = time.time()
    pool.close()
    pool.join()
    end = time.time()
    print(f"Elapsed time for async function: {end - start}")


def test(elem_count, test_num):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Test {test_num}; matrix: {elem_count} x {elem_count}")
    m1 = create_matrix(elem_count, elem_count)
    m2 = create_matrix(elem_count, elem_count)
    multiply_matrix(m1, m2)
    print("--------------------")
    multiply_matrix_async(m1, m2)


def main():
    test(10, 1)
    test(50, 2)
    test(100, 3)
    test(500, 4)
    test(600, 5)
    test(700, 6)


if __name__ == '__main__':
    main()
