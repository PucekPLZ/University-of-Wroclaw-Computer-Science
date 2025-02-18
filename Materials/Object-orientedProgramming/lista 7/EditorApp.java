import javax.swing.*;

public class EditorApp {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Editor App");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            JTabbedPane tabbedPane = new JTabbedPane();
            tabbedPane.addTab("Book", new BookEditor());
            tabbedPane.addTab("Publisher Current", new PublisherCurrentEditor());
            tabbedPane.addTab("Magazine", new MagazineEditor());

            frame.add(tabbedPane);
            frame.pack();
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });

        // Example usage of the FileUtils methods
        PublisherCurrent publisherCurrent = new PublisherCurrent("Effective Java", "Joshua Bloch", 350, "Addison-Wesley", 2018);
        Magazine magazine = new Magazine("JavaWorld", "John Doe", 80, "March 2023", 3);

        // Save objects to files
        FileUtils.saveObjectToFile(publisherCurrent, "publisherCurrent.ser");
        FileUtils.saveObjectToFile(magazine, "magazine.ser");

        // Load objects from files
        PublisherCurrent loadedPublisherCurrent = (PublisherCurrent) FileUtils.loadObjectFromFile("publisherCurrent.ser");
        Magazine loadedMagazine = (Magazine) FileUtils.loadObjectFromFile("magazine.ser");

        System.out.println("Loaded PublisherCurrent: " + loadedPublisherCurrent);
        System.out.println("Loaded Magazine: " + loadedMagazine);
    }
}