package componentes;

import java.awt.BorderLayout;
import java.awt.Font;

import javax.swing.ButtonGroup;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class exJRadioButton extends JFrame {
	
	private JPanel panel;
	private JRadioButton pc,pantalla,proyector;
	private ButtonGroup grupo;
	
	
	public exJRadioButton(){
		panel = new JPanel();
		grupo = new ButtonGroup();
		
		pc = new JRadioButton("PC",false);
		pantalla = new JRadioButton("Pantalla",false);
		proyector = new JRadioButton("Proyector",false);
		
		
		//Canviem el tipus de font
		pc.setFont(new Font("Arial",Font.PLAIN,20));
		pantalla.setFont(new Font("Arial",Font.PLAIN,20));
		proyector.setFont(new Font("Arial",Font.PLAIN,20));	
		
		
		//Anadir al grupo
		grupo.add(pc);
		grupo.add(pantalla);
		grupo.add(proyector);
		
		panel.add(pc);
		panel.add(pantalla);
		panel.add(proyector);
		
		this.add(panel,BorderLayout.CENTER);
		this.setTitle("JRadioButton... ");
		this.setSize(350, 200);
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}



	public static void main(String[] args) {
	
		new exJRadioButton();
	}

}