import javax.swing.*;
import java.awt.*;

public class MagazineEditor extends BookEditor {
    private JTextField issueField;
    private JTextField publicationMonthField;

    public MagazineEditor() {
        super();

        setLayout(new GridLayout(5, 2));

        add(new JLabel("Issue:"));
        issueField = new JTextField();
        add(issueField);

        add(new JLabel("Publication Month:"));
        publicationMonthField = new JTextField();
        add(publicationMonthField);
    }

    public Magazine getMagazine() {
        Book book = super.getBook();
        return new Magazine(
                book.getTitle(),
                book.getAuthor(),
                book.getPageCount(),
                issueField.getText(),
                Integer.parseInt(publicationMonthField.getText())
        );
    }
}
