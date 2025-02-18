package obliczenia;

public class Dzielenie extends Wyrazenie {
    private Wyrazenie left;
    private Wyrazenie right;

    public Dzielenie(Wyrazenie left, Wyrazenie right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public double oblicz() {
        double dzielnik = right.oblicz();
        if (dzielnik == 0) {
            throw new ArithmeticException("Division by zero");
        }
        return left.oblicz() / dzielnik;
    }

    @Override
    public String toString() {
        return "(" + left + " / " + right + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Dzielenie dzielenie = (Dzielenie) obj;
        return left.equals(dzielenie.left) && right.equals(dzielenie.right);
    }
}