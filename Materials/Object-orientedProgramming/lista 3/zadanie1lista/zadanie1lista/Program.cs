using System;
using zadanie1biblioteka;

namespace zadanie1
{
    internal class Program
    {
        static void Main()
        {
            Lista<int> llista = new Lista<int>();

            llista.push_back(1);
            llista.push_back(2);
            llista.push_back(3);
            llista.printLista();
            Console.WriteLine();

            llista.push_front(4);
            llista.push_front(5);
            llista.push_front(6);
            llista.printLista();
            Console.WriteLine();

            llista.pop_front();
            llista.pop_front();
            llista.pop_front();
            llista.printLista();
            Console.WriteLine();

            Console.WriteLine(llista.is_empty());

            llista.pop_back();
            llista.pop_back();
            llista.pop_back();
            llista.printLista();

            Console.WriteLine(llista.is_empty());
        }
    }
}




