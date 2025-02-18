package obliczenia;

public class Potega extends Wyrazenie {
    private Wyrazenie podstawa;
    private Wyrazenie wykladnik;

    public Potega(Wyrazenie podstawa, Wyrazenie wykladnik) {
        this.podstawa = podstawa;
        this.wykladnik = wykladnik;
    }

    @Override
    public double oblicz() {
        return Math.pow(podstawa.oblicz(), wykladnik.oblicz());
    }

    @Override
    public String toString() {
        return "(" + podstawa + "^" + wykladnik + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Potega potega = (Potega) obj;
        return podstawa.equals(potega.podstawa) && wykladnik.equals(potega.wykladnik);
    }
}