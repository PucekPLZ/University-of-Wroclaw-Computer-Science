package obliczenia;

public class Stala extends Wyrazenie {
    private double wartosc;

    public static final Stala PI = new Stala(Math.PI);
    public static final Stala E = new Stala(Math.E);

    public Stala(double wartosc) {
        this.wartosc = wartosc;
    }

    @Override
    public double oblicz() {
        return wartosc;
    }

    @Override
    public String toString() {
        return Double.toString(wartosc);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Stala stala = (Stala) obj;
        return Double.compare(stala.wartosc, wartosc) == 0;
    }
}