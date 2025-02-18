import java.util.Random;

public class BoardGenerator {
    private Board board;

    public BoardGenerator(Board board) {
        this.board = board;
    }

    public void setEmptyBoard() {
        int rows = board.getRows();
        int columns = board.getColumns();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                board.setCell(i, j, new Cell());
            }
        }
    }

        public void setFirstClickSafeBoard(int safeRow, int safeCol) {
        int rows = board.getRows();
        int columns = board.getColumns();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                board.setCell(i, j, new Cell());
            }
        }

        Random r = new Random();
        int n = 0;
        while (n < Constants.NUMBER_OF_MINES) {
            int randomX = r.nextInt(rows);
            int randomY = r.nextInt(columns);

            // Skip if this is the safe cell or one of its neighbors
            if ((Math.abs(randomX - safeRow) <= 1 && Math.abs(randomY - safeCol) <= 1)) {
                continue;
            }

            Cell cell = board.getCell(randomX, randomY);
            if (!cell.hasMine()) {
                cell.setHasMine(true);
                n++;

                // Update neighboring cells mine count
                for (int dx = -1; dx <= 1; dx++) {
                    for (int dy = -1; dy <= 1; dy++) {
                        int newX = randomX + dx;
                        int newY = randomY + dy;
                        if (board.isInBounds(newX, newY)) {
                            Cell neighbor = board.getCell(newX, newY);
                            if (!neighbor.hasMine()) {
                                neighbor.setMineCount(neighbor.getMineCount() + 1);
                            }
                        }
                    }
                }
            }
        }
    }
}
