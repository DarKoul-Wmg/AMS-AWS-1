package paint;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Paintliteral extends JFrame {
    private int lastX, lastY;
    private Color currentColor = Color.BLACK;

    public Paintliteral() {
        setTitle("Paint App");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel canvas = new JPanel();
        canvas.setBackground(Color.WHITE);

        canvas.addMouseListener(new MouseAdapter() {
            public void mousePressed(MouseEvent e) {
                lastX = e.getX();
                lastY = e.getY();
            }
        });

        canvas.addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseDragged(MouseEvent e) {
                Graphics g = canvas.getGraphics();
                g.setColor(currentColor);
                int x = e.getX();
                int y = e.getY();
                g.drawLine(lastX, lastY, x, y);
                lastX = x;
                lastY = y;
            }
        });

        JPanel colorPanel = new JPanel();
        colorPanel.setPreferredSize(new Dimension(50, 100));
        colorPanel.setBackground(Color.LIGHT_GRAY);

        JButton blackBtn = createColorButton(Color.BLACK);
        JButton redBtn = createColorButton(Color.RED);
        JButton blueBtn = createColorButton(Color.BLUE);
        JButton greenBtn = createColorButton(Color.GREEN);
        JButton clearBtn = new JButton("Clear Canvas");
        clearBtn.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                Graphics g = canvas.getGraphics();
                g.setColor(Color.WHITE);
                g.fillRect(0, 0, canvas.getWidth(), canvas.getHeight());
            }
        });

        colorPanel.add(blackBtn);
        colorPanel.add(redBtn);
        colorPanel.add(blueBtn);
        colorPanel.add(greenBtn);
        colorPanel.add(clearBtn);

        setLayout(new BorderLayout());
        add(canvas, BorderLayout.CENTER);
        add(colorPanel, BorderLayout.EAST);
    }

    private JButton createColorButton(Color color) {
        JButton button = new JButton();
        button.setBackground(color);
        button.setPreferredSize(new Dimension(30, 30));
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                currentColor = color;
            }
        });
        return button;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new Paintliteral().setVisible(true);
            }
        });
    }
}