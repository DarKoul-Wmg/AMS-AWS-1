package componentes;

import java.awt.Font;
import javax.swing.JComboBox;
import javax.swing.JFrame;

import javax.swing.JPanel;
import javax.swing.JSplitPane;
import javax.swing.JTabbedPane;
import javax.swing.JTextArea;


public class exJSplitPane extends JFrame {
	
	private JSplitPane panel;
	private JPanel panel1,panel2;
	private JComboBox cb;
	private JTextArea texto;
	
	public exJSplitPane(){
		cb= new JComboBox ();
				
		//Canviem el tipus de font
		cb.setFont(new Font("Arial",Font.PLAIN,20));	
		cb.addItem("WoW");
		cb.addItem("LoL");
		cb.addItem("Dark Souls");
		
		panel2 = new JPanel();
		panel2.add(cb);
		
		
		texto = new JTextArea("Escriu el teu nom",8,20);
		panel1 = new JPanel();
		panel1.add(texto);
		
		panel = new JSplitPane(JSplitPane.HORIZONTAL_SPLIT,panel1, panel2);
		panel.setOneTouchExpandable(true);
		
		this.add(panel);
		this.setTitle("JSplitPane... ");
		this.setSize(400, 250);
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}



	public static void main(String[] args) {
	
		new exJSplitPane();
	}

}

