// Lucjan Pucelak
// Visual Studio

using zadanie4;
using System;

namespace zadanie4wektor
{
    internal class Program
    {
        static void Main()
        {
            Wektor vector1 = new Wektor(3);
            vector1.fillVector(new float[] { 1, 2, 3 });

            Wektor vector2 = new Wektor(3);
            vector2.fillVector(new float[] { 1, 2, 3 });

            Console.Write(vector1.norma());
            Console.WriteLine();

            vector1.printVector();
            Console.WriteLine();

            Wektor sum = vector1.addVectors(vector2);
            sum.printVector();
            Console.WriteLine();

            Wektor sp = vector1.scalarProduct(vector2);
            sp.printVector();
            Console.WriteLine();

            Wektor multScalar = vector1.scalar(5);
            multScalar.printVector();
        }
    }
}


