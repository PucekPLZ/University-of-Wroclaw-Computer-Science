package obliczenia;

public class Wymierna implements Comparable<Wymierna> {
    private int licznik, mianownik = 1;

    public Wymierna(int l, int m) {
        if (m != 0) {
            this.licznik =  (m < 0) ? -l : l;
            this.mianownik = m; 

            reduceFraction();
        } else throw new IllegalArgumentException("Denominator equal to zero.");
    }

    public Wymierna(int n) {
        this(n, 1);
    }

    public Wymierna() {
        this.licznik = 0;
    }

    private int gcd(int a, int b) {
        if (b == 0) {
            return Math.abs(a);
        } else {
            return gcd(b, a % b);
        }
    }

    private void reduceFraction() {
        int commonDivisor = gcd(licznik, mianownik);
        licznik /= commonDivisor;
        mianownik /= commonDivisor;
    }

    public int getLicznik() {
        return licznik;
    }

    public int getMianownik() {
        return mianownik;
    }

    public void setLicznik(int licznik) {
        this.licznik = licznik;
    }

    public void setMianownik(int mianownik) {
        this.mianownik = mianownik;
    }

    public String toString() {
        String numberS = licznik + " / " + mianownik;
        return numberS;
    }

    public double toDouble() {
        return (double) licznik / mianownik;
    }

    public boolean equals(Wymierna other) {
        return this.licznik == other.licznik && this.mianownik == other.mianownik;
    }
    
    @Override
    public int compareTo(Wymierna other) {
        int thisNumerator = this.licznik * other.mianownik;
        int otherNumerator = other.licznik * this.mianownik;

        return Integer.compare(thisNumerator, otherNumerator);
    }

    public static Wymierna add(Wymierna left, Wymierna right) {
        int l = left.licznik * right.mianownik + right.licznik * left.mianownik;
        int m = left.mianownik * right.mianownik;

        return new Wymierna(l, m);
    }

    public static Wymierna sub(Wymierna left, Wymierna right) {
        int l = left.licznik * right.mianownik - right.licznik * left.mianownik;
        int m = left.mianownik * right.mianownik;

        return new Wymierna(l, m);
    }

    public static Wymierna mult(Wymierna left, Wymierna right) {
        int l = left.licznik * right.licznik;
        int m = left.mianownik * right.mianownik;
    
        return new Wymierna(l, m);
    }
    
    public static Wymierna div(Wymierna left, Wymierna right) {
        int l = left.licznik * right.mianownik;
        int m = left.mianownik * right.licznik;
    
        return new Wymierna(l, m);
    }    
}