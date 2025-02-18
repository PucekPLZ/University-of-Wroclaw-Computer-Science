package obliczenia;

public class Odwrotnosc extends Wyrazenie {
    private Wyrazenie wyrazenie;

    public Odwrotnosc(Wyrazenie wyr) {
        this.wyrazenie = wyr;
    }

    @Override
    public double oblicz() {
        double wartosc = wyrazenie.oblicz();
        if (wartosc == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return 1 / wartosc;
    }

    @Override
    public String toString() {
        return "(1 / " + wyrazenie + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Odwrotnosc odwrotnosc = (Odwrotnosc) obj;
        return wyrazenie.equals(odwrotnosc.wyrazenie);
    }
}