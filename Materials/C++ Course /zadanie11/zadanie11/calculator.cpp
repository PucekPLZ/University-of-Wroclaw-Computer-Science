#include "calculator.hpp"
#include "operator.hpp"

const std::set<std::string> keywords = { "print", "set", "to", "clear", "exit" };

Number::Number(double v) : value(v) {}
double Number::calculate() {
    return value;
}

std::map<std::string, double> Variable::variables;

Variable::Variable(const std::string& n) : name(n) {
    if (variables.find(name) == variables.end())
        variables[name] = 0;
    if (name.length() > 7 || keywords.find(name) != keywords.end()) {
        throw std::runtime_error("Invalid variable name");
    }
}

double Variable::calculate() {
    return variables[name];
}

Constant::Constant(const std::string& n) : name(n) {
    static std::map<std::string, double> constants {
        { "e", exp(1) },
        { "pi", acos(-1) },
        { "fi", (1 + sqrt(5)) / 2 }
    };
    if (constants.find(name) == constants.end()) {
        throw std::runtime_error("Unknown constant: " + name);
    }
    value = constants[name];
}

double Constant::calculate() {
    return value;
}

Symbol* getSymbolFromToken(const std::string& token) {
    if (token == "+") {
        return new kalkulator::Add(nullptr, nullptr);
    } else if (token == "-") {
        return new kalkulator::Subtract(nullptr, nullptr);
    } else if (token == "*") {
        return new kalkulator::Multiply(nullptr, nullptr);
    } else if (token == "/") {
        return new kalkulator::Divide(nullptr, nullptr);
    } else if (token == "%") {
        return new kalkulator::Modulo(nullptr, nullptr);
    } else if (token == "min") {
        return new kalkulator::Min(nullptr, nullptr);
    } else if (token == "max") {
        return new kalkulator::Max(nullptr, nullptr);
    } else if (token == "log") {
        return new kalkulator::Log(nullptr, nullptr);
    } else if (token == "pow") {
        return new kalkulator::Pow(nullptr, nullptr);
    } else if (token == "abs") {
        return new kalkulator::Abs(nullptr);
    } else if (token == "sgn") {
        return new kalkulator::Sgn(nullptr);
    } else if (token == "floor") {
        return new kalkulator::Floor(nullptr);
    } else if (token == "ceil") {
        return new kalkulator::Ceil(nullptr);
    } else if (token == "frac") {
        return new kalkulator::Frac(nullptr);
    } else if (token == "sin") {
        return new kalkulator::Sin(nullptr);
    } else if (token == "cos") {
        return new kalkulator::Cos(nullptr);
    } else if (token == "atan") {
        return new kalkulator::Atan(nullptr);
    } else if (token == "acot") {
        return new kalkulator::Acot(nullptr);
    } else if (token == "ln") {
        return new kalkulator::Ln(nullptr);
    } else if (token == "exp") {
        return new Exp(nullptr);
    } else {
        try {
            return new Number(std::stod(token));
        } catch (std::invalid_argument& e) {
            if (std::find_if(token.begin(), token.end(), [](unsigned char c) { return std::isalpha(c); }) == token.end()) {
                throw std::runtime_error("Unrecognized token: " + token);
            } else {
                static std::set<std::string> constants { "e", "pi", "fi" };
                if(constants.find(token) != constants.end()){
                    return new Constant(token);
                }else{
                    return new Variable(token);
                }
            }
        }
    }
}

double Exp::calculate() {
    return exp(operand->calculate());
}

double Expression::calculate() {
    std::stack<Symbol*> stack;
    try {
        while (!symbols.empty()) {
            Symbol* symbol = symbols.front();
            symbols.pop();
            Operator* op = dynamic_cast<Operator*>(symbol);
            if (op != nullptr) {
                if (stack.size() < 2) {
                    throw std::runtime_error("Not enough operands for operator");
                }
                op->right = stack.top(); stack.pop();
                op->left = stack.top(); stack.pop();
            }
            UnaryFunction* func = dynamic_cast<UnaryFunction*>(symbol);
            if (func != nullptr) {
                if (stack.empty()) {
                    throw std::runtime_error("Not enough operands for function");
                }
                func->operand = stack.top(); stack.pop();
            }
            stack.push(symbol);
        }
        if (stack.size() != 1) {
            throw std::runtime_error("Too many operands");
        }
        return stack.top()->calculate();
    } catch (...) {
        while (!stack.empty()) {
            delete stack.top();
            stack.pop();
        }
        throw;
    }
}

Expression::Expression(const std::string& expr) {
    std::istringstream iss(expr);
    std::string token;
    while (iss >> token) {
        symbols.push(getSymbolFromToken(token));
    }
}

PrintCommand::PrintCommand(const std::string& onp) : expression(onp) {}
void PrintCommand::execute() {
    std::cout << expression.calculate() << std::endl;
}

SetCommand::SetCommand(const std::string& name, const std::string& onp) : variableName(name), expression(onp) {}
void SetCommand::execute() {
    static std::set<std::string> constants { "e", "pi", "fi" };
    if (constants.find(variableName) != constants.end()) {
        std::clog << "Error: Cannot assign to a constant\n";
        return;
    }
    double value = expression.calculate();
    Variable::variables[variableName] = value;
    std::cout << value << std::endl;
}

void ClearCommand::execute() {
    Variable::variables.clear();
}
