package obliczenia;

public class Cos extends Wyrazenie {
    private Wyrazenie wartosc;

    public Cos(Wyrazenie wartosc) {
        this.wartosc = wartosc;
    }

    @Override
    public double oblicz() {
        return Math.cos(wartosc.oblicz());
    }

    @Override
    public String toString() {
        return "cos(" + wartosc + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Cos cos = (Cos) obj;
        return wartosc.equals(cos.wartosc);
    }
}