using System;

namespace zadanie1 
{
    public class IntStream {
        private int current = 0;
        private bool endOfStream = false;

        public virtual int next() {   
            if (endOfStream) {
                Console.WriteLine("End of a stream");
                return 0;
            }
            else {
                int result = current;
                current++;

                return result;
            }
            
        }

        public bool eos() {
            endOfStream = true;
            return endOfStream;
        }

        public virtual void reset() {
            current = 0;
            endOfStream = false;
        }
    }

    public class PrimeStream : IntStream {
        private int primeCurrent = 2;
        private bool endOfPrimeStream = false;

        public override int next() {
            while (!isPrime(primeCurrent)) {
                primeCurrent++;
            }

            if (eos(primeCurrent)) {
                Console.WriteLine("End of a prime stream");
                return 0;
            }
            else {
                int result = primeCurrent;
                primeCurrent++;

                return result;
            }
            
        }

        public bool eos(int primeNum) {
            if (primeNum > int.MaxValue) {
                endOfPrimeStream = true;
            }

            return endOfPrimeStream;
        }

        public override void reset() {
            primeCurrent = 2;
            endOfPrimeStream = false;
        }

        private bool isPrime(int n) {

            for (int i = 2; i <= Math.Sqrt(n); i++) {
                if (n % i == 0) {
                    return false;
                }
            }

            return true;
        }
    }

    public class RandomStream : IntStream {
        Random random = new Random();
        private int randomCurrent;
        

        public override int next() {
            randomCurrent = random.Next();
            int result = randomCurrent;
            
            return result;
        }

    }
    
    public class RandomWordStream {
        PrimeStream primeStreamForRandom = new PrimeStream();
        Random random = new Random();
        string letters = "abcdefghijklmnopqrstuvwxyz";

        public string next(){
            string randomWord = "";

            int length = primeStreamForRandom.next();

            for (int i = 0; i < length; i++) {
                randomWord += letters[random.Next(letters.Length)];
            }

            return randomWord;
        }
    }

    internal class Program {
        static void Main(string[] args) {
            IntStream stream = new IntStream();
            Console.WriteLine(stream.next());
            Console.WriteLine(stream.next());
            Console.WriteLine(stream.next());
            stream.eos();
            Console.WriteLine(stream.next());
            Console.WriteLine(stream.next());
            stream.reset();
            Console.WriteLine(stream.next());
            Console.WriteLine(stream.next());
            Console.WriteLine();

            PrimeStream primeStream = new PrimeStream();
            Console.WriteLine(primeStream.next());
            Console.WriteLine(primeStream.next());
            Console.WriteLine(primeStream.next());
            primeStream.reset();
            Console.WriteLine(primeStream.next());
            Console.WriteLine();

            RandomStream randomStream = new RandomStream();
            Console.WriteLine(randomStream.next());
            Console.WriteLine(randomStream.next());
            Console.WriteLine(randomStream.next());
            Console.WriteLine(randomStream.next());
            Console.WriteLine(randomStream.next());
            Console.WriteLine();

            RandomWordStream randomWordStream = new RandomWordStream();
            Console.WriteLine(randomWordStream.next());
            Console.WriteLine(randomWordStream.next());
            Console.WriteLine(randomWordStream.next());
            Console.WriteLine(randomWordStream.next());
        }
    }
}