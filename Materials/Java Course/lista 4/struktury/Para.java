package struktury;

public class Para implements Cloneable, Comparable<Para> {
    public final String klucz;
    private double wartosc;

    public Para(String key, double value) {
        this.klucz = key;
        this.wartosc = value;
    }

    public double getValue() {
        return wartosc;
    }

    public void setValue(double value) {
        this.wartosc = value;
    }

    @Override
    public String toString() {
        return "(" + klucz + ", " + wartosc + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Para other = (Para) obj;
        return klucz.equals(other.klucz);
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    @Override
    public int compareTo(Para other) {
        return this.klucz.compareTo(other.klucz);
    }
}