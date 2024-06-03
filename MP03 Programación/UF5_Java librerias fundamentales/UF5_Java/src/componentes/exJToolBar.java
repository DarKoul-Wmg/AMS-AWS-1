package componentes;

import java.awt.BorderLayout;
import java.awt.Font;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JButton;

import javax.swing.JPanel;
import javax.swing.JSplitPane;
import javax.swing.JTabbedPane;
import javax.swing.JTextArea;
import javax.swing.JToolBar;


public class exJToolBar extends JFrame {
	

	
	public exJToolBar(){
		JFrame ventanaPrincipal = new JFrame("JToolBar");
		JTextArea componentePrincipal = new JTextArea(25,80);
		JToolBar toolbar = getToolBar();
		
		ventanaPrincipal.add(componentePrincipal);
		ventanaPrincipal.add(toolbar,BorderLayout.NORTH);
		ventanaPrincipal.pack();
		ventanaPrincipal.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		ventanaPrincipal.setLocationRelativeTo(null);
		ventanaPrincipal.setVisible(true);
		
	}
	
	private JToolBar getToolBar() {
		JToolBar barraBotones = new JToolBar();
		barraBotones.add(new JButton("Boton 1"));
		barraBotones.add(new JButton("Boton 2"));
		barraBotones.add(new JButton("Boton 3"));
		barraBotones.add(new JButton("Boton 4"));
		
		return barraBotones;
	}



	public static void main(String[] args) {
	
		new exJToolBar();
	}

}

