package obliczenia;

public class Dodawanie extends Wyrazenie {
    private Wyrazenie left;
    private Wyrazenie right;

    public Dodawanie(Wyrazenie left, Wyrazenie right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public double oblicz() {
        return left.oblicz() + right.oblicz();
    }

    @Override
    public String toString() {
        return "(" + left + " + " + right + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Dodawanie dodawanie = (Dodawanie) obj;
        return left.equals(dodawanie.left) && right.equals(dodawanie.right);
    }
}