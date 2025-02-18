import java.util.Arrays;

public class zadanie4 {

    

    public static void mergeSort(Comparable[] array) throws InterruptedException {
        if (array.length < 2) {
            return;
        }

        int mid = array.length / 2;
        Comparable[] left = Arrays.copyOfRange(array, 0, mid);
        Comparable[] right = Arrays.copyOfRange(array, mid, array.length);

        MergeSortThread leftSortThread = new MergeSortThread(left);
        MergeSortThread rightSortThread = new MergeSortThread(right);

        leftSortThread.start();
        rightSortThread.start();

        leftSortThread.join();
        rightSortThread.join();

        merge(array, left, right);
    }

    public static void merge(Comparable[] array, Comparable[] left, Comparable[] right) {
        int i = 0, j = 0, k = 0;
    
        for (; i < left.length && j < right.length; k++) {
            if (left[i].compareTo(right[j]) <= 0) {
                array[k] = left[i++];
            } else {
                array[k] = right[j++];
            }
        }
    
        for (; i < left.length; i++, k++) {
            array[k] = left[i];
        }
    
        for (; j < right.length; j++, k++) {
            array[k] = right[j];
        }
    }
    

    static class MergeSortThread extends Thread {
        private final Comparable[] array;

        public MergeSortThread(Comparable[] array) {
            this.array = array;
        }

        public void run() {
            try {
                mergeSort(array);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }


    public static void main(String[] args) throws InterruptedException {
        Comparable[] array1 = new Comparable[]{3, 1, 7, 0, 4, 8, 2, 9, 6, 5};
        System.out.println(Arrays.toString(array1));
        mergeSort(array1);
        System.out.println(Arrays.toString(array1));

        System.out.println("");

        Comparable[] array2 = new Comparable[]{2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1};
        System.out.println(Arrays.toString(array2));
        mergeSort(array2);
        System.out.println(Arrays.toString(array2));
    }
}
