#include <iostream>
#include <stdexcept>
#include <cmath>
#include "wymierna.hpp"
using namespace::std;

int main() {
    obliczenia::wymierna w1(6, 8);
    obliczenia::wymierna w2(3, 4);

    double w1_double = static_cast<double>(w1);
    int w1_int = static_cast<int>(w1);
    
    obliczenia::wymierna w3 = w1 + w2;
    cout << "w3 licznik: " << w3.getLicznik() << endl;
    cout << "w3 mianownik: " << w3.getMianownik() << endl;

    cout << "w1 double: " << w1_double << endl;
    cout << "w1 int: " << w1_int << endl;
    
    obliczenia::wymierna w4 = w1 - w2;
    cout << "w4 licznik: " << w4.getLicznik() << endl;
    cout << "w4 mianownik: " << w4.getMianownik() << endl;
    
    obliczenia::wymierna w5 = w1 * w2;
    cout << "w5 licznik: " << w5.getLicznik() << endl;
    cout << "w6 mianownik: " << w5.getMianownik() << endl;

    obliczenia::wymierna w6 = w1 / w2;
    cout << "w6 licznik: " << w6.getLicznik() << endl;
    cout << "w6 mianownik: " << w6.getMianownik() << endl;
    
    obliczenia::wymierna w7 = -w1;
    cout << "w7 licznik: " << w7.getLicznik() << endl;
    cout << "w7 mianownik: " << w7.getMianownik() << endl;

    obliczenia::wymierna w8 = !w1;
    cout << "w8 licznik: " << w8.getLicznik() << endl;
    cout << "w8 mianownik: " << w8.getMianownik() << endl;
    
    obliczenia::wymierna w9(2359348, 99900);
    cout << "w9 ułamek dziesiętny okresowy: " << w9 << endl;
    
    return 0;
}
