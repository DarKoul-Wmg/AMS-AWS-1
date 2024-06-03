package componentes;


import java.awt.BorderLayout;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextArea;

public class exJTextArea extends JFrame {
	
	private JPanel panel;
	private JTextArea texto;
	
	public exJTextArea(){
		panel = new JPanel();
		
		texto = new JTextArea("Escribe algo",8,20);
		
		panel.add(texto);
		
		this.add(panel,BorderLayout.CENTER);
		this.setTitle("JTextAreas... ");
		this.pack();
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}
	
	
	
	public static void main(String[] args) {
		
		new exJTextArea();
	}

}
