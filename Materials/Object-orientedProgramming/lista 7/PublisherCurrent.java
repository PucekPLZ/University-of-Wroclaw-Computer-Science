import java.io.Serializable;

public class PublisherCurrent extends Book implements Serializable {
    private static final long serialVersionUID = 1L;

    private String publisher;
    private int yearPublished;

    public PublisherCurrent(String title, String author, int pageCount, String publisher, int yearPublished) {
        super(title, author, pageCount);
        this.publisher = publisher;
        this.yearPublished = yearPublished;
    }

    public String toString() {
        return "Wydawnictwo Ciagle " + publisher + " " + yearPublished + " " + super.toString();
    }
}
