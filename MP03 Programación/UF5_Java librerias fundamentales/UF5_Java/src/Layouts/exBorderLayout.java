package Layouts;

import java.awt.BorderLayout;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;

public class exBorderLayout extends JFrame {
	
	private JButton[] botones = new JButton[5];
	
	public exBorderLayout() {
		this.setSize(500,500);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		botones[0] = new JButton("Boton norte");
		ImageIcon imagen = new ImageIcon("./src/Layouts/Imagen1.jpg");
		botones[1] = new JButton(imagen);
		botones[2] = new JButton("img",imagen);
		botones[3] = new JButton("Boton este");
		botones[4] = new JButton("Boton oeste");
		
		//se deberia meter en un jpanel, pero se va a hacer directo al frame
		
		this.add(botones[0],BorderLayout.NORTH);
		this.add(botones[1],BorderLayout.CENTER);
		this.add(botones[2],BorderLayout.SOUTH);
		this.add(botones[3],BorderLayout.EAST);
		this.add(botones[4],BorderLayout.WEST);
		
		this.setVisible(true);
	}
	
	
	public static void main(String[] args) {
		
		//instanciamos directamente la clase
		new exBorderLayout();

	}

}
