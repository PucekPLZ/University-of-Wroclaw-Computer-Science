package algorithms;

import java.util.NoSuchElementException;

public interface Dictionary<T extends Comparable<T>> {
    
    boolean search(T x);
    void insert(T x);
    void remove(T x);

    T min() throws NoSuchElementException;
    T max() throws NoSuchElementException;

    public int size();
    public void clear();
}