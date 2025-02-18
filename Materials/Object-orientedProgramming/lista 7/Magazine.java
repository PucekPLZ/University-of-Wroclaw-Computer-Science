import java.io.Serializable;

public class Magazine extends Book implements Serializable {
    private static final long serialVersionUID = 1L;

    private String issue;
    private int publicationMonth;

    public Magazine(String title, String author, int pageCount, String issue, int publicationMonth) {
        super(title, author, pageCount);
        this.issue = issue;
        this.publicationMonth = publicationMonth;
    }

    public String toString() {
        return "Czasopismo " + issue + " " + publicationMonth + " " + super.toString();
    }
}
