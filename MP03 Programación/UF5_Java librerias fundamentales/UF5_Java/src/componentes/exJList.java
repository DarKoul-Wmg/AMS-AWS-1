package componentes;

import java.awt.BorderLayout;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class exJList extends JFrame {
	
	private JPanel panel;
	private JList lista;
	
	
	public exJList(){
		panel = new JPanel();
		String []datos = {"WOW", "LOL","DS"};
		lista = new JList (datos);
	
		panel.add(lista);
		
		this.add(panel,BorderLayout.CENTER);
		this.setTitle("JList... ");
		this.setSize(350, 200);
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}



	public static void main(String[] args) {
	
		new exJList();
	}

}


