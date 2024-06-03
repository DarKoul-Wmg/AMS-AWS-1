package componentes;

import java.awt.BorderLayout;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class exTextField extends JFrame {
	
	private JPanel panel;
	private JTextField texto;
	private JLabel nom;
	
	public exTextField(){
		panel = new JPanel();
		nom = new JLabel("Nom: ");
		texto = new JTextField(20);
	
		panel.add(nom);
		panel.add(texto);
		
		this.add(panel,BorderLayout.CENTER);
		this.setTitle("JTextField... ");
		this.setSize(350, 200);
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}



	public static void main(String[] args) {
	
		new exTextField();
	}

}

