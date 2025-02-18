package obliczenia;

public class Mnozenie extends Wyrazenie {
    private Wyrazenie left;
    private Wyrazenie right;

    public Mnozenie(Wyrazenie left, Wyrazenie right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public double oblicz() {
        return left.oblicz() * right.oblicz();
    }

    @Override
    public String toString() {
        return "(" + left + " * " + right + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Mnozenie mnozenie = (Mnozenie) obj;
        return left.equals(mnozenie.left) && right.equals(mnozenie.right);
    }
}