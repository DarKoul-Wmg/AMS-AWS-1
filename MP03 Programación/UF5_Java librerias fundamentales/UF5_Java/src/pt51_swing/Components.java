package pt51_swing;

import java.awt.BorderLayout;
import java.awt.GridLayout;

import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JRadioButton;
import javax.swing.JTabbedPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class Components extends JFrame {
	private JTabbedPane tabbedPane;
	private JPanel panelText,panelt1,panelt2,panelt3,panelt4,panelLista,panelEscoge;

    public Components() {
        setTitle("Interfície Gràfica");
        setSize(400, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        initComponents();
    }

    private void initComponents() {
        tabbedPane = new JTabbedPane();

        // Panel para la pestana Text
        panelText = new JPanel();
        panelText.setLayout(new GridLayout(4, 1));
        
        panelt1 = new JPanel();
        panelt2 = new JPanel();
        panelt3 = new JPanel();
        panelt4 = new JPanel();
        
        panelt1.add(new JLabel("JTextField"));
        panelt1.add(new JTextField(12));
        panelText.add(panelt1);
        
        panelt2.add(new JLabel("JPasswordField"));
        panelt2.add(new JPasswordField(12));
        panelText.add(panelt2);
        
        panelt3.add(new JLabel("JTextArea"));
        panelt3.add(new JTextArea(4,12));
        panelText.add(panelt3);
        
        panelt4.add(new JLabel("JLabel"));
        panelt4.add(new JLabel("Text"));
        panelText.add(panelt4);

        // Panel para la pestana JList
        panelLista = new JPanel();
        panelLista.setLayout(new BorderLayout());
        panelLista.add(new JList<>(new String[]{"Item 1", "Item 2", "Item 3"}));

        // Panel para la pestana Escull
        panelEscoge = new JPanel();
        panelEscoge.setLayout(new GridLayout(2, 1));
        panelEscoge.add(new JRadioButton("Opción 1"));
        
        // JComboBox inventado
        JComboBox<String> comboBox = new JComboBox<>(new String[]{"Opción A", "Opción B", "Opción C"});
        panelEscoge.add(comboBox);

        // Agregar paneles a las pestañas
        tabbedPane.addTab("Text", panelText);
        tabbedPane.addTab("JList", panelLista);
        tabbedPane.addTab("Escull", panelEscoge);

        getContentPane().add(tabbedPane); //se anade al frame

        setVisible(true);
    }

    public static void main(String[] args) {
        new Components();
    }
}
