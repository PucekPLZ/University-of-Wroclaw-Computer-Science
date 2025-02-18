package obliczenia;

public class Logarytm extends Wyrazenie {
    private Wyrazenie podstawa;
    private Wyrazenie argument;

    public Logarytm(Wyrazenie podstawa, Wyrazenie wykladnik) {
        this.podstawa = podstawa;
        this.argument = wykladnik;
    }

    @Override
    public double oblicz() {
        return Math.log(argument.oblicz()) / Math.log(podstawa.oblicz());
    }

    @Override
    public String toString() {
        return "log_" + podstawa + "(" + argument + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Logarytm logarytm = (Logarytm) obj;
        return podstawa.equals(logarytm.podstawa) && argument.equals(logarytm.argument);
    }
}