public class Minesweeper {
    public static void main(String[] args) {
        Board board = new Board(15, 15);
        BoardGenerator boardGenerator = new BoardGenerator(board);
        boardGenerator.setEmptyBoard();
        GUI gui = new GUI(board);
        GameController gameController = new GameController(board, gui);
        InputHandler inputHandler = new InputHandler(gameController, boardGenerator, gui);
        gui.setInputHandler(inputHandler);
    }
}

