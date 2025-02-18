public class GameController {
    private Board board;
    private GUI gui;
    private boolean gameOver = false;

    public GameController(Board board, GUI gui) {
        this.board = board;
        this.gui = gui;
    }

    public void processLeftClick(int x, int y) {
        if (board.isInBounds(x, y) && !gameOver) {
            board.revealCell(x, y);
            if (board.getCell(x, y).hasMine()) {
                // Game over, player lost
                revealAllMines();
                gameOver = true;
                gui.showGameOver(false);
            } else if (board.isAllNonMinesRevealed()) {
                // Game over, player won
                gui.showGameOver(true);
            } else {
                // Continue the game
                gui.repaint();
            }
        }
    }
    
    private void revealAllMines() {
        for (int i = 0; i < board.getRows(); i++) {
            for (int j = 0; j < board.getColumns(); j++) {
                Cell cell = board.getCell(i, j);
                if (cell.hasMine()) {
                    cell.setRevealed(true);
                }
            }
        }
    }    

    public void processRightClick(int x, int y) {
        if (board.isInBounds(x, y) && !gameOver) {
            board.toggleFlag(x, y);
            gui.repaint();
        }
    }
}
