package componentes;

import java.awt.BorderLayout;
import java.awt.Color;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class exJButton extends JFrame {
	private JPanel panel;
	private JButton b1, b2;
	
	
	public exJButton() {
		
		panel = new JPanel();
	
		ImageIcon imagen = new ImageIcon("./src/componentes/imagen.png");
		//color fondo
		b1 = new JButton(imagen);
		b2 = new JButton("Botó 2");
		
		b2.setBackground(Color.red);
		
		
		panel.add(b1);
		panel.add(b2);
		
		
		this.add(panel,BorderLayout.CENTER);
		this.setTitle("JButtons... ");
		this.pack();
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE); // Cierra automaticamente la ejecución en segundo plano de la ventana cuando se cierra


		
	}

	public static void main(String[] args) {
		new exJButton();

	}

}
