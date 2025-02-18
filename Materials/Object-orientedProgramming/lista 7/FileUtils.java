import java.io.*;

public class FileUtils {

    public static void saveObjectToFile(Object object, String filePath) {
        try (FileOutputStream fileOutputStream = new FileOutputStream(filePath);
             ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream)) {
            objectOutputStream.writeObject(object);
        } catch (IOException e) {
            System.err.println("Error saving object to file: " + e.getMessage());
        }
    }

    public static Object loadObjectFromFile(String filePath) {
        try (FileInputStream fileInputStream = new FileInputStream(filePath);
             ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream)) {
            return objectInputStream.readObject();
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Error loading object from file: " + e.getMessage());
            return null;
        }
    }
}

