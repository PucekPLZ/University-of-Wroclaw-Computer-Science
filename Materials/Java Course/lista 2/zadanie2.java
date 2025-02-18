class zadanie2 { 
    public static void main(String args[]) 
    { 
        try {
            LiczbyPierwsze classObj = new LiczbyPierwsze();

            long[] numbers = {23123123L, 123123L, -9223372036854775782L, 9223372036854775783L, -9223372036854775808L};

            for (int i = 0; i < numbers.length; i++) {
                System.out.print(numbers[i] + " = ");
            
                long[] fac = classObj.naCzynnikiPierwsze(numbers[i]);

                for (int j = 0; j < fac.length; j++) {
                    if (j != fac.length - 1) {
                        System.out.print(fac[j] + " * ");
                    } else {
                        System.out.print(fac[j] + "\n");
                    }
                }
            }
        } catch (Exception e) {
            System.err.print("Podaj parametry.");
        }
    } 
} 