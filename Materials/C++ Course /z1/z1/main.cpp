#include <iostream>
#include <vector>
#include <utility>

using namespace std;

const vector<pair<int, string> > rzym = {
    {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
    {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"},
    {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
};

int podajLiczbe(string l)
{
    int liczba;
    
    try
    {
        liczba = stoi(l);
        
    } catch (...)
    {
        clog << "Error: input nie jest poprawna liczba." << endl;
        return -1;
    }
    
    if (liczba > 3999 || liczba < 1)
        {
            clog << "Error: input nie jest poprawna liczba." << endl;
            return -1;
        }
        
    return liczba;
}

string int2rzym(int liczba)
{
    string rzymska;
    
    
    while (liczba>0)
    {
        for (int i = 0; i<=12; i++)
        {
            if (liczba >= rzym[i].first)
            {
                liczba -= rzym[i].first;
                rzymska += rzym[i].second;
                break;
            }
        }
    }
    
    return rzymska;
}

int main(int argc, const char * argv[])
{
    
    for (int i = 1; i < argc; i++)
    {
        if (podajLiczbe(argv[i]) != -1)
        {
            
            cout << int2rzym(podajLiczbe(argv[i])) << endl;
            
        }
    }
    
    
    return 0;
}

