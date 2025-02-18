#include <iostream>
#include "color.hpp"
#include "transparentColor.hpp"
#include "namedColor.hpp"
#include "colornt.hpp"
#include "pixel.hpp"
#include "coloredPixel.hpp"
#include <stdexcept>

using namespace std;

int main() {
    try {
        color kolor1(235, 76,13);
        cout << kolor1.getG_int() << endl;
        kolor1.setG(2);
        cout << kolor1.getG_int() << endl;
        color kolor2(12,43,67);
        kolor2.darken_color(12);
        cout << kolor2.getR_int() << " " << kolor2.getG_int() << " " << kolor2.getB_int() << endl;
        color kolor3(0,0,0);
        kolor3 = kolor3.mix_colors(kolor1, kolor2);
        cout << kolor3.getR_int() << " " << kolor3.getG_int() << " " << kolor3.getB_int() << endl;

        transparentColor kolor4(12,34,56, 243);
        cout << kolor4.getR_int() << " " << kolor4.getG_int() << " " << kolor4.getB_int() << " " << kolor4.getAlpha_int() << endl;

        namedColor kolor5(34, 56, 78, "lyga");
        cout << kolor5.getName() << endl;
        kolor5.setName("ala");
        cout << kolor5.getName() << endl;

        colornt kolor6(38, 45, 166, "milek", 178);
        cout << kolor6.getName() << endl;
        cout << kolor6.getAlpha_int() << endl;
        kolor6.setAlpha(56);
        cout << kolor6.getAlpha_int() << endl;
        
        transparentColor pixelColor1(100, 150, 200, 255);
        transparentColor pixelColor2(200, 100, 150, 255);
        coloredPixel pixel1(10, 20, pixelColor1);
        coloredPixel pixel2(50, 40, pixelColor2);
        
        int dist = distance(pixel1, pixel2);
        cout << dist << endl;
        pixel1.movePixel(5, 10);
        pixel2.movePixel(-5, 5);
        int dist1 = distance(pixel1, pixel2);
        cout << dist1 << endl;
        
    }
    catch (invalid_argument &e) {
        cerr << e.what();
    }

    return 0;
}
