package rozgrywka;

import obliczenia.Wymierna;

public class Gra {
    private int licznikPrób, maksIlośćPrób;
    private Wymierna liczba;
    private boolean aktywna;
    private double lowerLimit, upperLimit, maxLowerLimit, minUpperLimit;
    private String text; 

    public Gra() {
        aktywna = false;
    }

    public void start(int z) {
        if (z < 5 || z > 20) throw new IllegalArgumentException("Invalid range");

        int licz;
        int mian;

        // System.out.println(z);

        do {
            licz = (int) (Math.random() * z) + 1;
            mian = (int) (Math.random() * z) + 1;
        } while (licz >= mian);

        liczba = new Wymierna(licz, mian);
        maksIlośćPrób = (int) Math.ceil(3 * Math.log(z));
        licznikPrób = 0;
    
        assert licz < mian; // czy 0 < liczba < 1

        minUpperLimit = 1.0;
        maxLowerLimit = 0.0;

        System.out.println(liczba);

        aktywna = true;
    }

    public void makeGuess(Wymierna guess) {
        if (!aktywna) {
            throw new IllegalStateException("Game not active. Start a new game.");
        }

        licznikPrób++;
        int comparison = guess.compareTo(liczba);

        if (guess.equals(liczba)) {
            aktywna = false; 
            text = "Congratulations! The correct number was: " + liczba;
        } else if (licznikPrób >= maksIlośćPrób) {
            aktywna = false; 
            text = "Game over. The correct number was: " + liczba;
        } else {
            if (comparison < 0) {
                text = "Too few. Try again.";

                lowerLimit = guess.toDouble();
                if (maxLowerLimit < lowerLimit) {
                    maxLowerLimit = lowerLimit;
                }
                
            } else {
                text = "Too many. Try again.";

                upperLimit = guess.toDouble();
                if (minUpperLimit > upperLimit) {
                    minUpperLimit = upperLimit;
                }
            }
        }
    }

    public int getMaxAttempts() {
        return maksIlośćPrób;
    }

    public int getAttempts() {
        return licznikPrób;
    }

    public double getMaxLowerLimit() {
        return maxLowerLimit;
    }

    public double getMinUpperLimit() {
        return minUpperLimit;
    }

    public String getText() {
        return text;
    }
}