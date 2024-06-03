package componentes;

import java.awt.BorderLayout;

import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;

public class exJMenu extends JFrame {
	
	private JMenuBar menu;
	
	public exJMenu() {
		menu = new JMenuBar();
		
		JMenu arxiu = new JMenu("Arxiu"); 
		JMenuItem nou = new JMenuItem("Nou"); 
		arxiu.add(nou);
		
		JMenuItem obrir = new JMenuItem("Obrir"); 
		arxiu.add(obrir);
		
		JMenu editar=new JMenu("Editar"); 
		
		JMenuItem copiar = new JMenuItem("Copiar"); 
		editar.add(copiar);
		
		JMenuItem pegar=new JMenuItem("Pegar"); 
		editar.add(pegar);
		
		menu.add(arxiu);
		menu.add(editar);
	
	this.add(menu,BorderLayout.NORTH);
	this.setTitle("JMenu... ");
	this.setSize(300, 150);
	this.setVisible(true);
	
	setDefaultCloseOperation(EXIT_ON_CLOSE);
}



	public static void main(String[] args) {
	
		new exJMenu();
	}

}