import java.util.Scanner;

class zadanie1 {

    private static int[] arabskie = {
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
    };

    private static String[] rzymskie = {
        "M", "CM", "D", "CD", "C","XC", "L", "XL", "X", "IX", "V", "IV", "I"
    };

    private static String[] chinskie = {
        "małpa", "kurczak", "pies", "świnia", "szczur", "bawół", "tygrys", "królik", "smok", "wąż", "koń", "owca"
    };

    public static String rzymska(int n) {
        String nrzymskie = "";

        if (n <= 0 || n >= 4000) {
            throw new IllegalArgumentException("liczba " + n + " spoza zakresu 1-3999");
        } else {
            while (n > 0) {
                for (int i = 0; i <= rzymskie.length; i++) {
                    if (n >= arabskie[i]) {
                        n -= arabskie[i];
                        nrzymskie += rzymskie[i];
                        break;
                    }
                }
            }
        }

        return nrzymskie;
    }

    public static String patronChinski(int n) {
        String patron = chinskie[n % 12];
        
        return patron;
    }

    public static void main(String[] args) {
    Scanner imieObj = new Scanner(System.in); 
    System.out.println("Podaj swoje imię: ");

    String imie = imieObj.nextLine();  
    System.out.println("Cześć " + imie + "!");
    
    Scanner rokObj = new Scanner(System.in); 
    System.out.println("Podaj swój rok urodzenia: ");
    
    Integer rok = Integer.valueOf(rokObj.nextLine());  
    System.out.println("Twój rzymski rok to: " + rzymska(rok)); 
    System.out.println("Twój patron chiński to: " + patronChinski(rok));
    }
}