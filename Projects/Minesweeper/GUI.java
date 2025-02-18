import javax.swing.*;
import java.awt.*;
import javax.imageio.ImageIO;
import java.io.IOException;
import java.io.File;

public class GUI extends JFrame {
    private Board board;
    private Image flagImage;
    private Image bombImage;

    public GUI(Board board) {
        this.board = board;
        this.setTitle("Minesweeper");
        this.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        this.setSize(board.columns * Constants.CELL_SIZE + Constants.OFFSET_X * 2, board.rows * Constants.CELL_SIZE + Constants.OFFSET_Y + Constants.OFFSET_X);
        this.setLocationRelativeTo(null);
        this.setVisible(true);
        try {
            bombImage = ImageIO.read(new File("images/bomb.png"));
            flagImage = ImageIO.read(new File("images/flag.jpeg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private Color getNumberColor(int number) {
        switch (number) {
            case 1:
                return Color.BLUE;
            case 2:
                return Color.GREEN;
            case 3:
                return Color.RED;
            case 4:
                return new Color(0, 0, 128);
            case 5:
                return new Color(178, 34, 34); 
            case 6:
                return new Color(72, 209, 204); 
            case 7:
                return Color.BLACK;
            case 8:
                return Color.DARK_GRAY;
            default:
                return Color.BLACK;
        }
    }    

    public void setInputHandler(InputHandler inputHandler) {
        this.addMouseListener(inputHandler);
    }

    public void paint(Graphics g) {
        Graphics2D g2 = (Graphics2D) g;
        for (int i = 0; i < board.rows; i++) {
            for (int j = 0; j < board.columns; j++) {
                drawCell(g2, i, j);
            }
        }
    }

    private void drawCell(Graphics2D g2, int row, int col) {
        Cell cell = board.getCell(row, col);
        int x = Constants.OFFSET_X + col * Constants.CELL_SIZE;
        int y = Constants.OFFSET_Y + row * Constants.CELL_SIZE;
    
        if (cell.isCovered()) {
            g2.setColor(Color.lightGray);
        } else {
            g2.setColor(Color.white);
        }
        g2.fillRect(x, y, Constants.CELL_SIZE, Constants.CELL_SIZE);
        g2.setColor(Color.black);
        g2.drawRect(x, y, Constants.CELL_SIZE, Constants.CELL_SIZE);
        
        if (cell.isFlagged()) {
            g2.drawImage(flagImage, x, y, Constants.CELL_SIZE, Constants.CELL_SIZE, null);
        } else if (!cell.isCovered()) {
            if (cell.hasMine()) {
                g2.drawImage(bombImage, x, y, Constants.CELL_SIZE, Constants.CELL_SIZE, null);
            } else if (cell.getMineCount() > 0) {
                g2.setColor(getNumberColor(cell.getMineCount()));
                g2.drawString(String.valueOf(cell.getMineCount()), x + Constants.CELL_SIZE / 2 - 5, y + Constants.CELL_SIZE / 2 + 5);
            }
        } 
    }         

    public void showGameOver(boolean isWinner) {
        String message = isWinner ? "GGWP" : "Game over!";
        JOptionPane.showMessageDialog(this, message, "Minesweeper", JOptionPane.INFORMATION_MESSAGE);
    
        // Close the game after 5 seconds
        new Timer(5000, e -> this.dispose()).start();
    }      
}
