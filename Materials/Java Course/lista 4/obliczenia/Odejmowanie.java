package obliczenia;

public class Odejmowanie extends Wyrazenie {
    private Wyrazenie left;
    private Wyrazenie right;

    public Odejmowanie(Wyrazenie left, Wyrazenie right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public double oblicz() {
        return left.oblicz() - right.oblicz();
    }

    @Override
    public String toString() {
        return "(" + left + " - " + right + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Odejmowanie odejmowanie = (Odejmowanie) obj;
        return left.equals(odejmowanie.left) && right.equals(odejmowanie.right);
    }
}