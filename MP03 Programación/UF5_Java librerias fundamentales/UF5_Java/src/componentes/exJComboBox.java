package componentes;

import java.awt.BorderLayout;
import java.awt.Font;

import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class exJComboBox extends JFrame {
	
	private JPanel panel;
	private JComboBox cb;
	
	
	public exJComboBox(){
		panel = new JPanel();
		cb= new JComboBox ();
		
		
		//Canviem el tipus de font
		cb.setFont(new Font("Arial",Font.PLAIN,20));
		
		cb.addItem("WoW");
		cb.addItem("LoL");
		cb.addItem("Dark Souls");
		panel.add(cb);
		
		this.add(panel,BorderLayout.CENTER);
		this.setTitle("JComboBox... ");
		this.setSize(350, 200);
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}



	public static void main(String[] args) {
	
		new exJComboBox();
	}

}