import javax.swing.JPanel;
import java.time.LocalDate;

public class CalendarController {
    private CalendarModel model;
    private CalendarView view;

    public CalendarController(CalendarModel model, CalendarView view) {
        this.model = model;
        this.view = view;

        initController();
    }

    private void initController() {
        view.getPrevMonthButton().addActionListener(e -> navigateMonth(-1));
        view.getNextMonthButton().addActionListener(e -> navigateMonth(1));
        view.getYearSpinner().addChangeListener(e -> {
            int year = (Integer) view.getYearSpinner().getValue();
            navigateYear(year);
        });
    }

    private void navigateMonth(int delta) {
        model.navigateMonth(delta);
        updateView();
    }
    
    private void navigateYear(int year) {
        model.navigateYear(year);
        updateView();
    }
    
    private void updateView() {
        LocalDate calendarDate = model.getCalendarDate();
        JPanel yearPanel = view.createYearPanel(); 
        JPanel monthPanel = view.createThreeMonthPanel(calendarDate); 
        view.updateView(calendarDate, yearPanel, monthPanel);
    }    
}
