import javax.swing.*;
import java.awt.*;

public class BookEditor extends JComponent {
    private JTextField titleField;
    private JTextField authorField;
    private JTextField pageCountField;

    public BookEditor() {
        setLayout(new GridLayout(3, 2));

        add(new JLabel("Title:"));
        titleField = new JTextField();
        add(titleField);

        add(new JLabel("Author:"));
        authorField = new JTextField();
        add(authorField);

        add(new JLabel("Page Count:"));
        pageCountField = new JTextField();
        add(pageCountField);
    }

    public Book getBook() {
        return new Book(
                titleField.getText(),
                authorField.getText(),
                Integer.parseInt(pageCountField.getText())
        );
    }
}
