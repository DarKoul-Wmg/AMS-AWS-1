package componentes;

import java.awt.BorderLayout;
import java.awt.Color;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;



public class Jlabel_ImageIcon extends JFrame {
	private JPanel panel;
	private JLabel e1,e2;
	
	
	public Jlabel_ImageIcon() {
		
		panel = new JPanel();
		e1 = new JLabel("Etiqueta 1");
		
		//color fondo
		e1.setOpaque(true);
		e1.setBackground(Color.red);
		
		ImageIcon imagen = new ImageIcon("./src/componentes/imagen.png");
		
		e2 = new JLabel(imagen); //etiqueta con imagen
		panel.add(e1);
		panel.add(e2);
		this.add(panel,BorderLayout.CENTER);
		this.setTitle("JLabel e imagen");
		this.pack();
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE); // Cierra automaticamente la ejecución en segundo plano de la ventana cuando se cierra


		
	}
	
	public static void main(String[] args) {
		
		new Jlabel_ImageIcon();

	}

}
