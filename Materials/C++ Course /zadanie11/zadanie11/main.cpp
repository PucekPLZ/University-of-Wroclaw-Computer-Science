#include "operator.hpp"
#include "calculator.hpp"
using namespace std;

int main() {
    string line;
    while (getline(cin, line)) {
        istringstream iss(line);
        string token;
        if (!(iss >> token)) {
            continue;
        }

        try {
            if (token == "print") {
                string onp = line.substr(line.find(' ')+1);
                PrintCommand cmd(onp);
                cmd.execute();
            } else if (token == "set") {
                if (!(iss >> token)) {
                    clog << "Error: Missing variable name\n";
                    continue;
                }
                string name = token;
                string onp = line.substr(line.find(name)+name.length()+1);
                if (name.length() > 7) {
                    throw runtime_error("Invalid variable name");
                }
                SetCommand cmd(name, onp);
                cmd.execute();
            } else if (token == "clear") {
                ClearCommand cmd;
                cmd.execute();
            } else if (token == "exit") {
                break;
            } else {
                clog << "Unrecognized command: " << token << '\n';
            }
        } catch (runtime_error& e) {
            clog << "Error: " << e.what() << '\n';
        }
    }

    return 0;
}
