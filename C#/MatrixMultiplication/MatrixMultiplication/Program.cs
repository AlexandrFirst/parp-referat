using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading.Tasks;

namespace MatrixMultiplication
{
    class Program
    {
        static void Main(string[] args)
        {
            MultiplyMatrixTest multiplyMatrixTest = new MultiplyMatrixTest();
            multiplyMatrixTest.Run();
        }
    }

    class MultiplyMatrixTest
    {
        public void Run()
        {
            Test(10, 1);
            Test(100, 2);
            Test(500, 3);
            Test(600, 4);
            Test(700, 5);
        }

        private void Test(int matrixSize, int testNum)
        {
            Console.WriteLine($"Test num: {testNum}; matrix size: {matrixSize} x {matrixSize}");
            var m1 = GenerateMatrix(matrixSize, matrixSize);
            var m2 = GenerateMatrix(matrixSize, matrixSize);

            var syncMultResult = MatrixMultSync(m1, m2);

            var asyncMultResult = MatrixMultAsync(m1, m2);
            Console.WriteLine(new string('-', 48));
        }

        private List<List<Int64>> GenerateMatrix(int n, int m, int value = 0)
        {
            var data = new List<List<Int64>>();
            Random random = new Random();
            for (int i = 0; i < n; i++)
            {
                data.Add(new List<Int64>());
                for (int j = 0; j < m; j++)
                {
                    if (value == 0)
                        data[i].Add(random.Next(-1000, 1000));
                    else
                        data[i].Add(0);
                }
            }
            return data;
        }

        private List<List<Int64>> MatrixMultSync(List<List<Int64>> a, List<List<Int64>> b)
        {
            int n = a.Count;
            int m = b[0].Count;

            List<List<Int64>> result = GenerateMatrix(n, m, 0);

            var watch = new Stopwatch();
            watch.Start();

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    long tempSum = 0;
                    for (int k = 0; k < a[0].Count; k++)
                    {
                        tempSum += a[i][k] + b[k][j];
                    }
                    result[i][j] = tempSum;
                }
            }
            watch.Stop();
            Console.WriteLine($"Elapsed time for sync function: {watch.ElapsedMilliseconds / 1000.0}");
            return result;
        }

        private List<List<Int64>> MatrixMultAsync(List<List<Int64>> a, List<List<Int64>> b)
        {
            int n = a.Count;
            int m = b[0].Count;

            List<List<Int64>> result = GenerateMatrix(n, m, 0);
            List<Task> calculatingTasks = new List<Task>();

            var watch = new Stopwatch();
            watch.Start();

            for (int i = 0; i < n; i++)
            {
                var newRowCalcTask = calculateRowNums(a, b, i).ContinueWith(data =>
                {
                    (List<Int64>, int) taskResult = data.Result;
                    result[taskResult.Item2] = taskResult.Item1;
                });

                calculatingTasks.Add(newRowCalcTask);
            }

            Task.WaitAll(calculatingTasks.ToArray());
            watch.Stop();
            Console.WriteLine($"Elapsed time for async function: {watch.ElapsedMilliseconds / 1000.0}");

            return result;
        }

        private Task<(List<Int64>, int)> calculateRowNums(List<List<Int64>> a, List<List<Int64>> b, int lineIndex)
        {
            return Task<(List<Int64>, int)>.Factory.StartNew(() =>
            {
                List<Int64> row = new List<long>();
                for (int j = 0; j < b[0].Count; j++)
                {
                    long tempSum = 0;
                    for (int k = 0; k < a[0].Count; k++)
                    {
                        tempSum += a[lineIndex][k] + b[k][j];
                    }
                    row.Add(tempSum);
                }
                return (row, lineIndex);
            });
        }

        private void DisplayMatrix(List<List<Int64>> matrix)
        {
            matrix.ForEach(list =>
            {
                list.ForEach(item => Console.Write(item + " "));
                Console.WriteLine();
            });
        }
    }
}
