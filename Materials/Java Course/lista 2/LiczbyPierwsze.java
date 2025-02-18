import java.util.ArrayList;

public final class LiczbyPierwsze {
    private final static int POTEGA2 = 21;
    private final static int[] SITO = new int[1 << POTEGA2];

    static {
        for (int i = 2; i < SITO.length; i++) {
            if (SITO[i] == 0) {
                for (int j = i; j < SITO.length; j += i) {
                    if (SITO[j] == 0) {
                        SITO[j] = i;
                    }
                }
            }
        }
    }

    public static boolean czyPierwsza (long x) { 
        if (x <= 1) 
            return false; 

        long pierwiastek = (long) Math.sqrt(x);

        for (long i = 2; i <= pierwiastek; i++) {
            if (x % i == 0) 
                return false; 
        }

        return true; 
    }

    public static long[] naCzynnikiPierwsze (long x) {
        ArrayList<Long> factors = new ArrayList<>();
        long absX = Math.abs(x);

        while (absX > 1) {
            if (czyPierwsza(absX)) {
                factors.add(absX);
                break;
            }

            long i = 2;
            long smallestDivisor = 1;
            long pierwiastek = (long) Math.sqrt(absX);

            if (pierwiastek > SITO.length) {
                for (;i <= absX; i++) {
                    if (absX % i == 0) {
                        smallestDivisor = i;
                        break;
                    }
                }
            } else {
                while (i <= pierwiastek){
                    if (absX % SITO[(int) i] == 0) {
                        smallestDivisor = SITO[(int) i];
                        break;
                    }

                    i++;
                }
            }
            
            factors.add((long) smallestDivisor);
            absX /= smallestDivisor;
        }

        long[] result = new long[factors.size()];

        for (int i = 0; i < factors.size(); i++) {
            result[i] = factors.get(i);
        }

        return result;
    }
}
