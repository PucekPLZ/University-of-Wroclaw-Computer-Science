public class Board {
    int rows, columns;
    Cell[][] board;

    public Board(int n, int m) {
        rows = n;
        columns = m;
        board = new Cell[n][m];
    }

    public boolean isInBounds(int x, int y) {
        return x >= 0 && x < columns && y >= 0 && y < rows;
    }
    
    public Cell getCell(int x, int y) {
        return board[x][y];
    }
    
    public void revealCell(int x, int y) {
        Cell cell = getCell(x, y);
        if (!cell.isRevealed() && !cell.isFlagged()) {
            cell.setRevealed(true);
    
            if (cell.getValue() == 0) {
                // Reveal neighboring cells if the cell has no adjacent mines
                for (int dx = -1; dx <= 1; dx++) {
                    for (int dy = -1; dy <= 1; dy++) {
                        int newX = x + dx;
                        int newY = y + dy;
                        if (isInBounds(newX, newY)) {
                            revealCell(newX, newY);
                        }
                    }
                }
            }
        }
    }
    
    public void toggleFlag(int x, int y) {
        Cell cell = getCell(x, y);
        if (!cell.isRevealed()) {
            cell.setFlagged(!cell.isFlagged());
        }
    }
    
    public boolean isAllNonMinesRevealed() {
        for (int x = 0; x < columns; x++) {
            for (int y = 0; y < rows; y++) {
                Cell cell = getCell(x, y);
                if (!cell.hasMine() && !cell.isRevealed()) {
                    return false;
                }
            }
        }
        return true;
    }      

    public int getRows() {
        return rows;
    }
    
    public int getColumns() {
        return columns;
    }
    
    public void setCell(int x, int y, Cell cell) {
        board[x][y] = cell;
    }    

    public void setFlag(int y, int x) {
        Cell cell = getCell(x, y);
        cell.setFlagged(!cell.isFlagged());
    }    
}
