package obliczenia;

public class Negacja extends Wyrazenie {
    private Wyrazenie wyrazenie;

    public Negacja(Wyrazenie wyr) {
        this.wyrazenie = wyr;
    }

    @Override
    public double oblicz() {
        return -wyrazenie.oblicz();
    }

    @Override
    public String toString() {
        return "-(" + wyrazenie + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Negacja negacja = (Negacja) obj;
        return wyrazenie.equals(negacja.wyrazenie);
    }
}