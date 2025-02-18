package obliczenia;

public abstract class Wyrazenie implements Obliczalny, Cloneable {

    public static double suma(Wyrazenie... wyr) {
        double wynik = 0;
        for (Wyrazenie wyrazenie : wyr) {
            wynik += wyrazenie.oblicz();
        }
        return wynik;
    }

    public static double iloczyn(Wyrazenie... wyr) {
        double result = 1; 
        for (Wyrazenie expression : wyr) {
            result *= expression.oblicz();
        }
        return result;
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
}