public class Cell {
    private int state;      // 0: covered, 1: uncovered, 2: flagged
    private int mineCount;  // number of mines around the cell
    private boolean hasMine;

    public Cell() {
        this.state = 0;
        this.mineCount = 0;
        this.hasMine = false;
    }

    // Getters
    public int getState() {
        return state;
    }

    public int getMineCount() {
        return mineCount;
    }

    public int getValue() {
        return hasMine ? -1 : mineCount;
    }

    public boolean hasMine() {
        return hasMine;
    }

    // Setters
    public void setState(int state) {
        if (state >= 0 && state <= 2) {
            this.state = state;
        } else {
            throw new IllegalArgumentException("Invalid state value. Must be 0, 1, or 2.");
        }
    }

    public void setMineCount(int mineCount) {
        if (mineCount >= 0 && mineCount <= 8) {
            this.mineCount = mineCount;
        } else {
            throw new IllegalArgumentException("Invalid mine count value. Must be between 0 and 8 inclusive.");
        }
    }

    public void setHasMine(boolean hasMine) {
        this.hasMine = hasMine;
    }

    public void setRevealed(boolean revealed) {
        state = revealed ? 1 : 0;
    }
    
    public void setFlagged(boolean flagged) {
        state = flagged ? 2 : 0;
    }

    public boolean isCovered() {
        return state == 0;
    }
    
    public boolean isFlagged() {
        return state == 2;
    }

    public boolean isRevealed() {
        return state == 1;
    }
}
