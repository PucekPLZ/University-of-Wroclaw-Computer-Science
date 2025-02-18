package obliczenia;

public class Test {
    public static void main(String[] args) {
        
        Zmienna.dodajZmienna("x", 1.618);

        Wyrazenie wyrazenie1 = new Odejmowanie(
                new Dodawanie(
                        new Liczba(7),
                        new Mnozenie(
                                new Liczba(5),
                                new Liczba(3)
                        )
                ),
                new Liczba(1)
        );

        Wyrazenie wyrazenie2 = new Mnozenie(
                new Negacja( 
                    new Odejmowanie(
                        new Liczba(2),
                        new Zmienna("x")
                    )
                ),
                Stala.E
        );

        Wyrazenie wyrazenie3 = new Dzielenie(
                new Odejmowanie(
                        new Mnozenie(
                                new Liczba(3),
                                Stala.PI
                        ),
                        new Liczba(1)
                ),
                new Dodawanie(
                        new Zmienna("x"),
                        new Liczba(5)
                )
        );

        Wyrazenie wyrazenie4 = new Sin(
                new Dzielenie(
                        new Dodawanie(
                                new Zmienna("x"),
                                new Liczba(13)
                        ),
                        new Odejmowanie(
                                new Liczba(1),
                                new Zmienna("x")
                        )
                )
        );

        Wyrazenie wyrazenie5 = new Dodawanie(
                new Potega(
                        new Liczba(5), 
                        new Liczba(1)
                ),
                new Mnozenie(
                        new Zmienna("x"),
                        new Logarytm(
                                Stala.E,
                                new Zmienna("x")
                        )
                )
        );

        System.out.println("Wyrazenie 1: " + wyrazenie1);
        System.out.println("Wyrazenie 2: " + wyrazenie2);
        System.out.println("Wyrazenie 3: " + wyrazenie3);
        System.out.println("Wyrazenie 4: " + wyrazenie4);
        System.out.println("Wyrazenie 5: " + wyrazenie5);

        try {
            Wyrazenie klonWyrazenia1 = (Wyrazenie) wyrazenie1.clone();
            Wyrazenie klonWyrazenia2 = (Wyrazenie) wyrazenie2.clone();
            Wyrazenie klonWyrazenia3 = (Wyrazenie) wyrazenie3.clone();
            Wyrazenie klonWyrazenia4 = (Wyrazenie) wyrazenie4.clone();
            Wyrazenie klonWyrazenia5 = (Wyrazenie) wyrazenie5.clone();

            System.out.println("Klon wyrazenia 1: " + klonWyrazenia1);
            System.out.println("Klon wyrazenia 2: " + klonWyrazenia2);
            System.out.println("Klon wyrazenia 3: " + klonWyrazenia3);
            System.out.println("Klon wyrazenia 4: " + klonWyrazenia4);
            System.out.println("Klon wyrazenia 5: " + klonWyrazenia5);

            System.out.println("Czy takie same: " + wyrazenie1.equals(klonWyrazenia1));
            System.out.println("Czy takie same: " + wyrazenie2.equals(klonWyrazenia2));
            System.out.println("Czy takie same: " + wyrazenie3.equals(klonWyrazenia3));
            System.out.println("Czy takie same: " + wyrazenie4.equals(klonWyrazenia4));
            System.out.println("Czy takie same: " + wyrazenie5.equals(klonWyrazenia5));
            
            double wynik1 = wyrazenie1.oblicz();
            double wynik2 = wyrazenie2.oblicz();
            double wynik3 = wyrazenie3.oblicz();
            double wynik4 = wyrazenie4.oblicz();
            double wynik5 = wyrazenie5.oblicz();

            System.out.println("Wynik wyrazenia 1: " + wynik1);
            System.out.println("Wynik wyrazenia 2: " + wynik2);
            System.out.println("Wynik wyrazenia 3: " + wynik3);
            System.out.println("Wynik wyrazenia 4: " + wynik4);
            System.out.println("Wynik wyrazenia 5: " + wynik5);
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }
    }
}