import javax.swing.*;
import javax.swing.border.TitledBorder;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class CalendarView {
    private CalendarModel model;
    private Color backgroundColor;
	private JComboBox<String> monthComboBox;
    private JFrame frame;
    private JToolBar toolbar;
	private JLabel[][] dayLabel;
	private JLabel titleLabel;
	private JTextField dayField;
	private JTextField yearField;
    private JTabbedPane tabbedPane;
    private JSpinner yearSpinner;
    private JButton btnPrevMonth, btnNextMonth;
    private static final String[] DAY_NAMES = { "Mon", "Tue",
			"Wed", "Thu", "Fri", "Sat", "Sun" };
	private static final String[] MONTH_NAMES = { "January", "February", 
			"March", "April", "May", "June", "July",
			"August", "September", "October", "November", "December" };

    public CalendarView(CalendarModel model) {
        this.model = model;
        initializeComponents();
    }

    private void initializeComponents() {
        frame = new JFrame("Calendar");
        tabbedPane = new JTabbedPane();

        toolbar = createToolbar();

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());
        frame.add(tabbedPane, BorderLayout.CENTER);
        frame.add(toolbar, BorderLayout.PAGE_END);
    }

    public void createAndShowGUI() {
        frame.pack();
        frame.setLocationByPlatform(true);
        frame.setVisible(true);
    }

    public JPanel createYearPanel() {
        JPanel yearPanel = new JPanel(new GridLayout(3, 4)); 

        for (int i = 0; i < 12; i++) {
            int monthIndex = i;
            JPanel monthPanel = createMonthPanel(monthIndex, false, model.calendarDate.getYear());
            TitledBorder titleBorder = new TitledBorder(MONTH_NAMES[monthIndex]);
            monthPanel.setBorder(titleBorder);

            monthPanel.addMouseListener(new MouseAdapter() {
                @Override
                public void mouseClicked(MouseEvent e) {
                    switchToMonthTab(monthIndex, true);
                }
            });
            
            yearPanel.add(monthPanel);
        }

        return yearPanel;
    }

    public JPanel createMonthPanel(int monthIndex, boolean showDayNames, int year) {
        int rows = showDayNames ? 7 : 6;
        JPanel panel = new JPanel(new GridLayout(rows, 7, 10, 10)); 
    
        if (showDayNames) {
            for (String dayName : DAY_NAMES) {
                JLabel dayLabel = new JLabel(dayName);
                dayLabel.setHorizontalAlignment(JLabel.CENTER);
                panel.add(dayLabel);
            }
        }
    
        LocalDate date = LocalDate.of(year, monthIndex + 1, 1);
        int dayOfWeek = date.getDayOfWeek().getValue();
    
        int offset = (dayOfWeek - 1);
        for (int i = 0; i < offset; i++) {
            panel.add(new JLabel("")); 
        }
    
        LocalDate today = LocalDate.now();
        while (date.getMonth().ordinal() == monthIndex) {
            JLabel dayLabel = new JLabel(Integer.toString(date.getDayOfMonth()));
            dayLabel.setHorizontalAlignment(JLabel.CENTER);

            if (date.equals(today)) {
                dayLabel.setOpaque(true);
                dayLabel.setBackground(Color.YELLOW);
            } 
            
            if (date.getDayOfWeek() == DayOfWeek.SUNDAY) {
                dayLabel.setForeground(Color.RED);
            } else {
                dayLabel.setForeground(Color.BLACK); 
            }

            panel.add(dayLabel);
            date = date.plusDays(1);
        }
    
        while (panel.getComponentCount() < rows * 7) {
            panel.add(new JLabel(""));
        }
    
        return panel;
    }    

    private void switchToMonthTab(int monthIndex, boolean switchTab) {
        LocalDate selectedMonth = LocalDate.of(model.calendarDate.getYear(), monthIndex + 1, 1);
        JPanel monthsPanel = createThreeMonthPanel(selectedMonth);
        
        if (tabbedPane.getTabCount() > 1) {
            tabbedPane.setTitleAt(1, MONTH_NAMES[monthIndex]);
            tabbedPane.setComponentAt(1, monthsPanel);
            if (switchTab) {
                tabbedPane.setSelectedIndex(1); 
            }
        } else {
            tabbedPane.addTab(MONTH_NAMES[monthIndex], monthsPanel);
            if (switchTab) {
                tabbedPane.setSelectedIndex(1); 
            }
        }
    }       

    public JPanel createThreeMonthPanel(LocalDate date) {
        JPanel panel = new JPanel(new GridLayout(1, 3));
        
        LocalDate previousMonth = date.minus(1, ChronoUnit.MONTHS);
        LocalDate nextMonth = date.plus(1, ChronoUnit.MONTHS);
    
        JPanel prevMonthPanel = createMonthPanel(previousMonth.getMonthValue() - 1, true, previousMonth.getYear());
        String prevMonthTitle = MONTH_NAMES[previousMonth.getMonthValue() - 1] + " " + previousMonth.getYear();
        prevMonthPanel.setBorder(new TitledBorder(prevMonthTitle));
        panel.add(prevMonthPanel);
    
        JPanel currentMonthPanel = createMonthPanel(date.getMonthValue() - 1, true, date.getYear());
        String currentMonthTitle = MONTH_NAMES[date.getMonthValue() - 1] + " " + date.getYear();
        currentMonthPanel.setBorder(new TitledBorder(currentMonthTitle));
        panel.add(currentMonthPanel);

        JPanel nextMonthPanel = createMonthPanel(nextMonth.getMonthValue() - 1, true, nextMonth.getYear());
        String nextMonthTitle = MONTH_NAMES[nextMonth.getMonthValue() - 1] + " " + nextMonth.getYear();
        nextMonthPanel.setBorder(new TitledBorder(nextMonthTitle));
        panel.add(nextMonthPanel);
    
        return panel;
    }           
	
	public void updateDayLabels() {
		int month = monthComboBox.getSelectedIndex();
		int day = valueOf(dayField.getText().trim());
		int year = valueOf(yearField.getText().trim());
		
		if (year > 0 && day > 0) {
			LocalDate monthDate = model.getPreviousSaturday(year, month);
			fillDays(monthDate, year, month, day);	
			
			String title = MONTH_NAMES[month] + " " + year;
			titleLabel.setText(title);
		} 
	}  

	private void fillDays(LocalDate monthDate, int year, int month, int day) {
        for (int j = 0; j < dayLabel.length; j++) {
            for (int i = 0; i < dayLabel[j].length; i++) {
                int calMonth = monthDate.getMonth().ordinal();
                int calYear = monthDate.getYear();
                dayLabel[j][i].getParent().setBackground(backgroundColor);
                dayLabel[j][i].setText(" ");
    
                if (year == calYear && month == calMonth) {
                    int calDay = monthDate.getDayOfMonth();
                    dayLabel[j][i].setText(Integer.toString(calDay));
                    
                    if (monthDate.getDayOfWeek() == java.time.DayOfWeek.SUNDAY) {
                        dayLabel[j][i].getParent().setBackground(Color.RED);
                    }

                    if (day == calDay) {
                        dayLabel[j][i].getParent().setBackground(Color.YELLOW);
                    }
                }
                monthDate = monthDate.plusDays(1L);
            }
        }
    }    
	
	public int valueOf(String text) {
		try {
			return Integer.valueOf(text);
		} catch (NumberFormatException e) {
			return -1;
		}
	}

    private JToolBar createToolbar() {
        JToolBar toolbar = new JToolBar();

        btnPrevMonth = new JButton("<");
        btnNextMonth = new JButton(">");

        SpinnerModel yearModel = new SpinnerNumberModel(model.getCalendarDate().getYear(), 1, 2100, 1);
        yearSpinner = new JSpinner(yearModel);
        yearSpinner.setPreferredSize(new Dimension(100, 20));

        toolbar.add(btnPrevMonth);
        toolbar.add(yearSpinner);
        toolbar.add(btnNextMonth);

        return toolbar;
    }

    public JButton getPrevMonthButton() {
        return btnPrevMonth;
    }

    public JButton getNextMonthButton() {
        return btnNextMonth;
    }

    public JSpinner getYearSpinner() {
        return yearSpinner;
    }

    public JTabbedPane getTabbedPane() {
        return tabbedPane;
    }

    public void updateView(LocalDate calendarDate, JPanel yearPanel, JPanel monthPanel) {
        tabbedPane.setComponentAt(0, yearPanel);
        tabbedPane.setTitleAt(0, Integer.toString(calendarDate.getYear())); 
        if (tabbedPane.getTabCount() > 1) {
            tabbedPane.setComponentAt(1, monthPanel);
            String monthTitle = MONTH_NAMES[calendarDate.getMonthValue() - 1];
            tabbedPane.setTitleAt(1, monthTitle); 
        }
    
        yearSpinner.setValue(calendarDate.getYear());
    }    

    public void initializeAndUpdateView() {
        JPanel yearPanel = createYearPanel();
        JPanel monthPanel = createThreeMonthPanel(model.getCalendarDate());
        tabbedPane.addTab("Year", yearPanel);
        tabbedPane.addTab("Month", monthPanel);
        updateView(model.getCalendarDate(), yearPanel, monthPanel);
    }    
}