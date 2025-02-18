import javax.swing.SwingUtilities;

public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            CalendarModel model = new CalendarModel();
            CalendarView view = new CalendarView(model);
            CalendarController controller = new CalendarController(model, view);

            view.initializeAndUpdateView();
            view.createAndShowGUI();
        });
    }
}