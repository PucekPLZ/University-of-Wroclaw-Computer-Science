import javax.swing.*;
import java.awt.*;

public class PublisherCurrentEditor extends BookEditor {
    private JTextField publisherField;
    private JTextField yearPublishedField;

    public PublisherCurrentEditor() {
        super();

        setLayout(new GridLayout(5, 2));

        add(new JLabel("Publisher:"));
        publisherField = new JTextField();
        add(publisherField);

        add(new JLabel("Year Published:"));
        yearPublishedField = new JTextField();
        add(yearPublishedField);
    }

    public PublisherCurrent getPublisherCurrent() {
        Book book = super.getBook();
        return new PublisherCurrent(
                book.getTitle(),
                book.getAuthor(),
                book.getPageCount(),
                publisherField.getText(),
                Integer.parseInt(yearPublishedField.getText())
        );
    }
}

