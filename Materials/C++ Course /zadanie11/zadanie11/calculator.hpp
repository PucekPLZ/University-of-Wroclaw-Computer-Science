#pragma once
#include "operator.hpp"
#include <queue>
#include <string>
#include <sstream>
#include <map>
#include <stack>
#include <cmath>
#include <algorithm>
#include <set>

class Symbol;

class Operand : public Symbol {
};

class Number : public Operand {
    double value;
public:
    Number(double v);
    double calculate() override;
};

class Variable : public Operand {
public:
    static std::map<std::string, double> variables;
    std::string name;
    Variable(const std::string& n);
    double calculate() override;
};

class Constant : public Operand {
    std::string name;
    double value;
public:
    Constant(const std::string& n);
    double calculate() override;
};

Symbol* getSymbolFromToken(const std::string& token);

class Expression {
    std::queue<Symbol*> symbols;
public:
    Expression(const std::string& onp);
    double calculate();
};

class Exp : public UnaryFunction {
public:
    Exp(Symbol* o) : UnaryFunction(o) {}
    double calculate() override;
};

class Command {
public:
    virtual void execute() = 0;
};

class PrintCommand : public Command {
    Expression expression;
public:
    PrintCommand(const std::string& onp);
    void execute() override;
};

class SetCommand : public Command {
    std::string variableName;
    Expression expression;
public:
    SetCommand(const std::string& name, const std::string& onp);
    void execute() override;
};

class ClearCommand : public Command {
public:
    void execute() override;
};

