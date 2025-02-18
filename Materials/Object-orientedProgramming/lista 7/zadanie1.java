public class zadanie1 {
    public static void main(String[] args) {
        PublisherCurrent publisherCurrent = new PublisherCurrent("Effective Java", "Joshua Bloch", 350, "Addison-Wesley", 2018);
        Magazine magazine = new Magazine("JavaWorld", "John Doe", 80, "March 2023", 3);

        System.out.println(publisherCurrent);
        System.out.println(magazine);
    }
}

