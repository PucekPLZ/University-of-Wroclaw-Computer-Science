#include <iostream>
#include "tabbit.hpp"

using namespace std;

int main() {
    try {
        tab_bit mytab = tab_bit(46);
        tab_bit u(16ull);
        tab_bit v(mytab);
        tab_bit w(8, {1, 0, 1, 1, 0, 0, 0, 1});
        
        cout << "mytab: " << mytab << endl;
        cout << "u: " << u << endl;
        cout << "v: " << v << endl;
        cout << "w: " << w << endl;
        
        mytab[1] = 1;
        mytab[2] = 1;
        mytab[5] = 1;
        mytab[40] = true;
        mytab[45] = true;
        cout << "mytab: " << mytab << endl;
        
        bool z = mytab[1];
        cout << "value: " << z << endl;
        
        mytab[40] = mytab[34] = mytab[3] = 1;
        cout << "mytab: " << mytab << endl;
        
        tab_bit a(8, {1, 0, 1, 1, 0, 0, 0, 1});
        tab_bit b(8, {1, 1, 0, 0, 1, 1, 0, 0});
        tab_bit c = a;
        tab_bit d = b;

        c &= b;
        d |= a;

        cout << "a & b: " << c << endl;
        cout << "a | b: " << d << endl;

        tab_bit e = a;
        tab_bit f = b;

        e ^= b;
        f = ~f;

        cout << "a ^ b: " << e << endl;
        cout << "~b: " << f << endl;
        
    } catch (const InvalidSizeException& e) {
        cerr << "Error: " << e.what() << endl;
        return 1;
    } catch (const InvalidIndexException& e) {
        cerr << "Error: " << e.what() << endl;
        return 1;
    } catch (const std::exception& e) {
        cerr << "Error: " << e.what() << endl;
        return 1;
    }
    
    return 0;
}
