import javax.swing.*;
import java.awt.*;

import algorithms.*;

public class Window extends JFrame {
    private BST<String> bst;
    private BSTPanel bstPanel;

    public Window() {
        super("BST");
        bst = new BST<>();
        bstPanel = new BSTPanel();

        JButton insertButton = new JButton("Insert");
        JButton removeButton = new JButton("Remove");
        JButton searchButton = new JButton("Search");
        JButton minButton = new JButton("Find Min");
        JButton maxButton = new JButton("Find Max");
        JButton clearButton = new JButton("Clear");
        JButton sizeButton = new JButton("Size");

        JTextField inputField = new JTextField(15);

        insertButton.addActionListener(e -> handleInsert(inputField.getText()));
        removeButton.addActionListener(e -> handleRemove(inputField.getText()));
        searchButton.addActionListener(e -> handleSearch(inputField.getText()));
        minButton.addActionListener(e -> handleMin());
        maxButton.addActionListener(e -> handleMax());
        clearButton.addActionListener(e -> handleClear());
        sizeButton.addActionListener(e -> handleSize());

        JPanel controlPanel = new JPanel();
        controlPanel.add(new JLabel("Enter Value: "));
        controlPanel.add(inputField);
        controlPanel.add(insertButton);
        controlPanel.add(removeButton);
        controlPanel.add(searchButton);
        controlPanel.add(minButton);
        controlPanel.add(maxButton);
        controlPanel.add(clearButton);
        controlPanel.add(sizeButton);

        setLayout(new BorderLayout());
        add(controlPanel, BorderLayout.NORTH);
        add(bstPanel, BorderLayout.CENTER);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1000, 600);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void handleInsert(String value) {
        if (!value.isEmpty()) {
            try {
                bst.insert(value);
                bstPanel.repaint();
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Invalid input.");
            }
        }
    }
    
    private void handleRemove(String value) {
        if (!value.isEmpty()) {
            try {
                bst.remove(value);
                bstPanel.repaint();
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Invalid input.");
            }
        }
    }

    private void handleSearch(String value) {
        if (!value.isEmpty()) {
            try {
                boolean found = bst.search(value);
                JOptionPane.showMessageDialog(this, "Element found: " + found);
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Invalid input.");
            }
        }
    }    

    private void handleMin() {
        try {
            String minValue = bst.min();
            JOptionPane.showMessageDialog(this, "Minimum value: " + minValue);
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "BST is empty");
        }
    }
    
    private void handleMax() {
        try {
            String maxValue = bst.max();
            JOptionPane.showMessageDialog(this, "Maximum value: " + maxValue);
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "BST is empty");
        }
    }    

    private void handleClear() {
        bst.clear();
        bstPanel.repaint();
    }

    private void handleSize() {
        int sizeValue = bst.size();
        JOptionPane.showMessageDialog(this, "Maximum value: " + sizeValue);
    }

    private class BSTPanel extends JPanel {
        @Override
        public void paintComponent(Graphics g) {
            super.paintComponent(g);
            drawBST(g, getWidth() / 2, 50, bst.root, getWidth() / 4, 0);
        }
    
        private void drawBST(Graphics g, int x, int y, BST.Node node, int xOffset, int level) {
            if (node != null) {
                g.drawString(node.value.toString(), x, y);
    
                int nextLevel = level + 1;
                int nextXOffset = xOffset / 2;
    
                if (node.left != null) {
                    int xLeft = x - xOffset;
                    int yLeft = y + 50;
                    g.drawLine(x, y, xLeft, yLeft);
                    drawBST(g, xLeft, yLeft, node.left, nextXOffset, nextLevel);
                }
    
                if (node.right != null) {
                    int xRight = x + xOffset;
                    int yRight = y + 50;
                    g.drawLine(x, y, xRight, yRight);
                    drawBST(g, xRight, yRight, node.right, nextXOffset, nextLevel);
                }
            }
        }
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(Window::new);
    }
}