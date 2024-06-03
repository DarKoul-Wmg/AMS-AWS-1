package componentes;

import java.awt.BorderLayout;
import java.awt.Font;

import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class exJTabbedPane extends JFrame {
	

	private JComboBox cb;
	private JTabbedPane panel1,panel2;
	private JTextArea texto;
	
	public exJTabbedPane(){
		panel1 = new JTabbedPane();
		cb= new JComboBox ();
		
		
		//Canviem el tipus de font
		cb.setFont(new Font("Arial",Font.PLAIN,20));	
		cb.addItem("WoW");
		cb.addItem("LoL");
		cb.addItem("Dark Souls");
		
		JPanel panel2 = new JPanel();
		panel2.add(cb);
		
		panel1.addTab("Primera pestana", panel2);
		
		texto = new JTextArea("Escriu el teu nom",8,20);
		
		panel1.addTab("Segona pestana", texto);
		
		this.add(panel1);
		this.setTitle("JTabbedPane... ");
		this.setSize(400, 250);
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}



	public static void main(String[] args) {
	
		new exJTabbedPane();
	}

}
