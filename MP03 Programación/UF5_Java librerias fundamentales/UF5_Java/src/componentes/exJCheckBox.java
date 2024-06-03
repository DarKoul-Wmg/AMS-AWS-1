package componentes;

import java.awt.BorderLayout;
import java.awt.Font;

import javax.swing.ButtonGroup;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class exJCheckBox extends JFrame {
	
	private JPanel panel;
	private JCheckBox pc,pantalla,proyector;

	
	
	public exJCheckBox(){
		panel = new JPanel();

		
		pc = new JCheckBox("PC",false);
		pantalla = new JCheckBox("Pantalla",false);
		proyector = new JCheckBox("Proyector",false);
		
		
		//Canviem el tipus de font
		pc.setFont(new Font("Arial",Font.PLAIN,20));
		pantalla.setFont(new Font("Arial",Font.PLAIN,20));
		proyector.setFont(new Font("Arial",Font.PLAIN,20));	
		
		
		
		panel.add(pc);
		panel.add(pantalla);
		panel.add(proyector);
		
		this.add(panel,BorderLayout.CENTER);
		this.setTitle("JCheckBox... ");
		this.setSize(350, 200);
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}



	public static void main(String[] args) {
	
		new exJCheckBox();
	}

}
