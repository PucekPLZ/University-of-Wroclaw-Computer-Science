package struktury;

public interface Zbior {

    Para search(String k);

    void insert(Para p);

    void remove(String k);

    void clear();

    int size();
}