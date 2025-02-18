package prezentacja;

import java.awt.*;
import java.awt.event.*;
import obliczenia.Wymierna;
import rozgrywka.Gra;

public class Okno extends Frame implements ActionListener, AdjustmentListener {
    private TextField licznik, mianownik;
    private Button guessButton, newGameButton, endGameButton, quitButton;
    private Scrollbar attemptsScrollbar, rangeScrollbar;
    private Gra gra;
    private Label scopeLabel, textLabel;

    public Okno() {
        setTitle("Fraction Guessing Game");
        setSize(214, 300);
        setLayout(new FlowLayout());
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent we) {
                System.exit(0);
            }
        });

        initializeComponents();
        setComponentsState(false);

        setVisible(true);
    }

    private void initializeComponents() {
        licznik = new TextField(5);
        mianownik = new TextField(5);

        guessButton = new Button("Guess");
        newGameButton = new Button("New Game");
        endGameButton = new Button("End Game");
        quitButton = new Button("Quit");

        rangeScrollbar = new Scrollbar(Scrollbar.HORIZONTAL, 5, 1, 5, 21);
        attemptsScrollbar = new Scrollbar(Scrollbar.HORIZONTAL, 0, 1, 0, 1);

        scopeLabel = new Label("Scope: ");
        textLabel = new Label("Text: ");

        guessButton.addActionListener(this);
        newGameButton.addActionListener(this);
        endGameButton.addActionListener(this);
        quitButton.addActionListener(this);

        attemptsScrollbar.addAdjustmentListener(this);
        rangeScrollbar.addAdjustmentListener(this);

        add(new Label("Numerator:"));
        add(licznik);
        add(new Label("Denominator:"));
        add(mianownik);
        add(guessButton);
        add(newGameButton);
        add(endGameButton);
        add(quitButton);
        add(new Label("Attempts:"));
        add(attemptsScrollbar);
        add(new Label("Range:"));
        add(rangeScrollbar);
        add(scopeLabel);
        add(textLabel);
    }

    private void setComponentsState(boolean active) {
        guessButton.setEnabled(active);
        newGameButton.setEnabled(!active);
        endGameButton.setEnabled(active);
        licznik.setEnabled(active);
        mianownik.setEnabled(active);
        attemptsScrollbar.setEnabled(active);
        rangeScrollbar.setEnabled(!active); 
    }

    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == guessButton) {
            int numerator = Integer.parseInt(licznik.getText());
            int denominator = Integer.parseInt(mianownik.getText());
            Wymierna guess = new Wymierna(numerator, denominator);

            gra.makeGuess(guess);
            updateUI();
        } else if (ae.getSource() == newGameButton) {
            int zakres = rangeScrollbar.getValue();

            gra = new Gra();
            gra.start(zakres);
            setComponentsState(true);
            updateUI();
        } else if (ae.getSource() == endGameButton) {
            setComponentsState(false);
            updateUI();
        } else if (ae.getSource() == quitButton) {
            System.exit(0); 
        }
    }

    public void adjustmentValueChanged(AdjustmentEvent e) {
    }

    private void updateUI() {
        attemptsScrollbar.setMaximum(gra.getMaxAttempts());
        attemptsScrollbar.setValue(gra.getAttempts());

        scopeLabel.setText("[ " + gra.getMaxLowerLimit() + ", " + gra.getMinUpperLimit() + " ]");
        textLabel.setText(gra.getText());
    }

    public static void main(String[] args) {
        new Okno();
    }
}