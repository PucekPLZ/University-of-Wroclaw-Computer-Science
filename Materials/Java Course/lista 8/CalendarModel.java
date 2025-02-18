import java.time.LocalDate;

public class CalendarModel {
    public LocalDate calendarDate;

    public CalendarModel() {
        this.calendarDate = LocalDate.now();
    }

    public LocalDate getCalendarDate() {
        return calendarDate;
    }

    public void setCalendarDate(LocalDate calendarDate) {
        this.calendarDate = calendarDate;
    }

    public LocalDate getPreviousSaturday(int year, int month) {
        LocalDate monthDate = LocalDate.of(year, month + 1, 1);
        int weekday = monthDate.getDayOfWeek().ordinal();
        monthDate = monthDate.minusDays(weekday % 7);
        return monthDate;
    }

    public void navigateMonth(int delta) {
        calendarDate = calendarDate.plusMonths(delta);
    }

    public void navigateYear(int year) {
        calendarDate = LocalDate.of(year, calendarDate.getMonth(), calendarDate.getDayOfMonth());
    }
}