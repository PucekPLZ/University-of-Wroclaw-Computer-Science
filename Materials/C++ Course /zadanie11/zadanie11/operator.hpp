#pragma once
#include <cmath>
#include <stdexcept>
#include <iostream>

class Symbol {
public:
    virtual double calculate() = 0;
};

class Operator : public Symbol {
public:
    Symbol* left;
    Symbol* right;
public:
    Operator(Symbol* l, Symbol* r) : left(l), right(r) {}
    virtual ~Operator() {
        delete left;
        delete right;
    }
};

class UnaryFunction : public Symbol {
public:
    Symbol* operand;
    UnaryFunction(Symbol* o) : operand(o) {}
    virtual ~UnaryFunction() {
        delete operand;
    }
};

namespace kalkulator {
    class Add : public Operator {
    public:
        Add(Symbol* l, Symbol* r);
        double calculate() override;
    };

    class Subtract : public Operator {
    public:
        Subtract(Symbol* l, Symbol* r);
        double calculate() override;
    };

    class Multiply : public Operator {
    public:
        Multiply(Symbol* l, Symbol* r);
        double calculate() override;
    };

    class Divide : public Operator {
    public:
        Divide(Symbol* l, Symbol* r);
        double calculate() override;
    };

    // Binary functions

    class Modulo : public Operator {
    public:
        Modulo(Symbol* l, Symbol* r);
        double calculate() override;
    };

    class Min : public Operator {
    public:
        Min(Symbol* l, Symbol* r);
        double calculate() override;
    };

    class Max : public Operator {
    public:
        Max(Symbol* l, Symbol* r);
        double calculate() override;
    };

    class Log : public Operator {
    public:
        Log(Symbol* l, Symbol* r);
        double calculate() override;
    };

    class Pow : public Operator {
    public:
        Pow(Symbol* l, Symbol* r);
        double calculate() override;
    };

    // Unary functions

    class Abs : public UnaryFunction {
    public:
        Abs(Symbol* o);
        double calculate() override;
    };

    class Sgn : public UnaryFunction {
    public:
        Sgn(Symbol* o);
        double calculate() override;
    };

    class Floor : public UnaryFunction {
    public:
        Floor(Symbol* o);
        double calculate() override;
    };

    class Ceil : public UnaryFunction {
    public:
        Ceil(Symbol* o);
        double calculate() override;
    };

    class Frac : public UnaryFunction {
    public:
        Frac(Symbol* o);
        double calculate() override;
    };

    class Sin : public UnaryFunction {
    public:
        Sin(Symbol* o);
        double calculate() override;
    };

    class Cos : public UnaryFunction {
    public:
        Cos(Symbol* o);
        double calculate() override;
    };

    class Atan : public UnaryFunction {
    public:
        Atan(Symbol* o);
        double calculate() override;
    };

    class Acot : public UnaryFunction {
    public:
        Acot(Symbol* o);
        double calculate() override;
    };

    class Ln : public UnaryFunction {
    public:
        Ln(Symbol* o);
        double calculate() override;
    };
}

