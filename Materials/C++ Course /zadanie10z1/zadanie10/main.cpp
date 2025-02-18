#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include "manipulatory.hpp"
using namespace::std;

vector<std::string> readLines(istream& is) {
    vector<std::string> lines;
    string line;

    while(getline(is, line)) {
        lines.push_back(line);
    }

    return lines;
}

void sortAndPrintLines(vector<string>& lines) {
    vector<std::pair<int, string>> indexedLines;
    int index = 0;

    for(const auto& line : lines) {
        indexedLines.push_back({index++, line});
    }

    sort(indexedLines.begin(), indexedLines.end(),
        [](const pair<int, string>& a, const pair<int, string>& b) {
            return a.second < b.second;
        }
    );

    for(const auto& indexedLine : indexedLines) {
        cout << "[" << indexedLine.first << "]: " << indexedLine.second << '\n';
    }
}

int main() {
    vector<string> lines = readLines(cin);
    sortAndPrintLines(lines);
        
    cout << lines[1] << colon << lines[2] << "\n\n";
    cout << lines[1] << comma << lines[2] << "\n\n";
    cout << index_manip(2, 3) << colon << lines[2] << "\n\n";
        
    stringstream ss;
    ss << "Line to ignore\nLine to keep";

    cout << "Before clearline: \n" << ss.str() << "\n\n";

    clearline(ss);

    string remaining;
    getline(ss, remaining, '\0');
    cout << "After clearline: \n" << remaining << '\n';
    
    ss.str("Character to ignore Rest of the line");
    ss.clear();
    cout << "\nBefore ignore: \n" << ss.str() << "\n\n";
    ss >> ignore_manip(20);

    getline(ss, remaining);
    cout << "After ignore: \n" << remaining << '\n';
    
    return 0;
}
