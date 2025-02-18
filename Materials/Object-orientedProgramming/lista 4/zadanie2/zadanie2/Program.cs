using System;
using System;
using System.Collections;
using System.Collections.Generic;

namespace MyApp 
{

    public class SlowaFibonacciego : IEnumerable<string>
    {
        private int length;

        public SlowaFibonacciego(int n)
        {
            length = n;
        }

        public IEnumerator<string> GetEnumerator()
        {
            
            string prev1 = "";
            string prev2 = "";

            for (int x = 0; x <= length; x++)
            {
                string current = "";

                if (x == 1)
                {
                    current = "b";
                }
                else if (x == 2)
                {
                    current = "a";
                }
                else
                {
                    current = prev2 + prev1;
                }

                yield return current;

                prev1 = prev2;
                prev2 = current;
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }


    internal class Program 
    {
        static void Main(string[] args)
        {
            SlowaFibonacciego sf = new SlowaFibonacciego(7);
            foreach (string s in sf)
                Console.WriteLine(s);
        }
    }
}