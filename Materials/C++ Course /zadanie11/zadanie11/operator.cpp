#include "operator.hpp"

using namespace kalkulator;

Add::Add(Symbol* l, Symbol* r) : Operator(l, r) {}
double Add::calculate() {
    return left->calculate() + right->calculate();
}

Subtract::Subtract(Symbol* l, Symbol* r) : Operator(l, r) {}
double Subtract::calculate() {
    return left->calculate() - right->calculate();
}

Multiply::Multiply(Symbol* l, Symbol* r) : Operator(l, r) {}
double Multiply::calculate() {
    return left->calculate() * right->calculate();
}

Divide::Divide(Symbol* l, Symbol* r) : Operator(l, r) {}
double Divide::calculate() {
    double rightVal = right->calculate();
    if (rightVal == 0) {
        std::clog << "Error: Division by zero.\n";
        return 0;
    }
    return left->calculate() / rightVal;
}

// Binary functions

Modulo::Modulo(Symbol* l, Symbol* r) : Operator(l, r) {}
double Modulo::calculate() {
    double rightVal = right->calculate();
    if (rightVal == 0) {
        std::clog << "Error: Modulo by zero.\n";
        return 0;
    }
    return fmod(left->calculate(), rightVal);
}

Min::Min(Symbol* l, Symbol* r) : Operator(l, r) {}
double Min::calculate() {
    return std::min(left->calculate(), right->calculate());
}

Max::Max(Symbol* l, Symbol* r) : Operator(l, r) {}
double Max::calculate() {
    return std::max(left->calculate(), right->calculate());
}

Log::Log(Symbol* l, Symbol* r) : Operator(l, r) {}
double Log::calculate() {
    double rightVal = right->calculate();
    if (rightVal <= 0) {
        std::clog << "Error: Log base must be positive and not equal to 1.\n";
        return 0;
    }
    return log(left->calculate()) / log(rightVal);
}

Pow::Pow(Symbol* l, Symbol* r) : Operator(l, r) {}
double Pow::calculate() {
    return pow(left->calculate(), right->calculate());
}

// Unary functions

Abs::Abs(Symbol* o) : UnaryFunction(o) {}
double Abs::calculate() {
    return abs(operand->calculate());
}

Sgn::Sgn(Symbol* o) : UnaryFunction(o) {}
double Sgn::calculate() {
    double val = operand->calculate();
    return (val > 0) - (val < 0);
}

Floor::Floor(Symbol* o) : UnaryFunction(o) {}
double Floor::calculate() {
    return floor(operand->calculate());
}

Ceil::Ceil(Symbol* o) : UnaryFunction(o) {}
double Ceil::calculate() {
    return ceil(operand->calculate());
}

Frac::Frac(Symbol* o) : UnaryFunction(o) {}
double Frac::calculate() {
    double val = operand->calculate();
    return val - floor(val);
}

Sin::Sin(Symbol* o) : UnaryFunction(o) {}
double Sin::calculate() {
    return sin(operand->calculate());
}

Cos::Cos(Symbol* o) : UnaryFunction(o) {}
double Cos::calculate()  {
    return cos(operand->calculate());
}

Atan::Atan(Symbol* o) : UnaryFunction(o) {}
double Atan::calculate() {
    return atan(operand->calculate());
}

Acot::Acot(Symbol* o) : UnaryFunction(o) {}
double Acot::calculate() {
    double val = operand->calculate();
    return (val != 0) ? atan(1 / val) : 0;
}

Ln::Ln(Symbol* o) : UnaryFunction(o) {}
double Ln::calculate() {
    double val = operand->calculate();
    if (val <= 0) {
        std::clog << "Error: Natural log of non-positive number.\n";
        return 0;
    }
    return log(val);
}
