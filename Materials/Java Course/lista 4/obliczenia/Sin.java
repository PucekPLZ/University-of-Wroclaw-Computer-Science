package obliczenia;

public class Sin extends Wyrazenie {
    private Wyrazenie wartosc;

    public Sin(Wyrazenie wartosc) {
        this.wartosc = wartosc;
    }

    @Override
    public double oblicz() {
        return Math.sin(wartosc.oblicz());
    }

    @Override
    public String toString() {
        return "sin(" + wartosc + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Sin sin = (Sin) obj;
        return wartosc.equals(sin.wartosc);
    }
}