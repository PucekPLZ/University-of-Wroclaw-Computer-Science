using System;

namespace Zadanie3 {   
    public class LazyIntList {
        private List<int> elements;

        public LazyIntList() {
            elements = new List<int>();
        }

        // element musi byc liczba dodatnia
        public virtual int element(int i) {

            if (elements.Count >= i) {
                    return elements[i - 1];
                }

            for (int j = elements.Count + 1; j <= i; j++) {
                    elements.Add(j);
                }
                return elements[i - 1];
            }

        public int size() {
            return elements.Count;
        } 
    }

    public class LazyPrimeList : LazyIntList {
        public override int element(int i) {

                int numPrimes = 0;

                for (int j = 2; ; j++) {
                    if (isPrime(j)) {
                        numPrimes++;

                        if (numPrimes == i) {
                            return j;
                        }
                    }       
                }
            }

        private bool isPrime(int n) {
                if (n < 2) {
                    return false;
                }

                for (int i = 2; i <= Math.Sqrt(n); i++) {
                    if (n % i == 0) {
                        return false;
                    }
                }

                return true;
            }
        }


    internal class Program {   
        static void Main(string[] args) {
            LazyIntList list = new LazyIntList();
            Console.WriteLine(list.element(35));
            Console.WriteLine(list.size());
            Console.WriteLine(list.element(38));
            Console.WriteLine(list.size());
            Console.WriteLine(list.element(35));
            Console.WriteLine();

            LazyPrimeList primeList = new LazyPrimeList();
            Console.WriteLine(primeList.element(2));
            Console.WriteLine(primeList.element(4));
            Console.WriteLine(primeList.element(2));
        }
    }
}