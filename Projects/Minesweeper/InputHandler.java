import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingUtilities;

public class InputHandler extends MouseAdapter {
    private GUI gui;
    private GameController gameController;
    private BoardGenerator boardGenerator;
    private int counter = 0;

    public InputHandler(GameController gameController, BoardGenerator boardGenerator, GUI gui) {
        this.gameController = gameController;
        this.boardGenerator = boardGenerator;
        this.gui = gui;
    }

    @Override
    public void mouseClicked(MouseEvent e) {
        int x, y;

        x = (e.getX() - Constants.OFFSET_X) / Constants.CELL_SIZE;
        y = (e.getY() - Constants.OFFSET_Y) / Constants.CELL_SIZE;
        if (SwingUtilities.isLeftMouseButton(e)) {
            if (counter == 0) {
                boardGenerator.setFirstClickSafeBoard(y, x);
                counter++;
            }
            gameController.processLeftClick(y, x);
        }
        if (SwingUtilities.isRightMouseButton(e)) {
            gameController.processRightClick(y, x);
        }

        gui.repaint();
    }
}
