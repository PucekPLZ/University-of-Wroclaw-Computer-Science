package obliczenia;
import struktury.ZbiorTablicowy;
import struktury.Para;

public class Zmienna extends Wyrazenie {
    private static final ZbiorTablicowy zbiorZmiennych = new ZbiorTablicowy(10);
    private final String id;

    public Zmienna(String id) {
        this.id = id;
    }

    public static void dodajZmienna(String id, double value) {
        Para para = new Para(id, value);
        zbiorZmiennych.insert(para);
    }

    public static double getValue(String id) {
        Para para = zbiorZmiennych.search(id);
        return para.getValue();
    }

    public static void setValue(String id, double value) {
        Para para = zbiorZmiennych.search(id);
        para.setValue(value);
    }

    @Override
    public double oblicz() {
        Para para = zbiorZmiennych.search(id);
        return para.getValue();
    }

    @Override
    public String toString() {
        return id;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        Zmienna zmienna = (Zmienna) obj;
        return id.equals(zmienna.id);
    }
}