package struktury;
import java.util.Arrays;

public class ZbiorTablicowy implements Zbior, Cloneable {
    private Para[] zbior;
    private int zapelnienie;

    public ZbiorTablicowy(int size) {
        this.zbior = new Para[size];
        this.zapelnienie = 0;
    }

    @Override
    public Para search(String k) {
        for (Para para : zbior) {
            if (para != null && para.klucz.equals(k)) {
                return para;
            }
        }
        return null;
    }

    @Override
    public void insert(Para p) {
        if (zapelnienie == zbior.length) {
            throw new IllegalStateException("Table is completely filled");
        }

        Para istniejacaPara = search(p.klucz);
        if (istniejacaPara != null) {
            istniejacaPara.setValue(p.getValue());
        } else {
            zbior[zapelnienie++] = p;
        }
    }

    @Override
    public void remove(String k) {
        for (int i = 0; i < zapelnienie; i++) {
            if (zbior[i] != null && zbior[i].klucz.equals(k)) {
                zbior[i] = null;
                zapelnienie--;
                compactArray();
                return;
            }
        }
    }

    private void compactArray() {
        int currentIndex = 0;
        for (int i = 0; i < zapelnienie; i++) {
            if (zbior[i] != null) {
                zbior[currentIndex++] = zbior[i];
            }
        }
        Arrays.fill(zbior, currentIndex, zapelnienie, null);
    }

    @Override
    public void clear() {
        Arrays.fill(zbior, null);
        zapelnienie = 0;
    }

    @Override
    public int size() {
        return zapelnienie;
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        ZbiorTablicowy clone = (ZbiorTablicowy) super.clone();
        clone.zbior = Arrays.copyOf(zbior, zbior.length);
        return clone;
    }
}