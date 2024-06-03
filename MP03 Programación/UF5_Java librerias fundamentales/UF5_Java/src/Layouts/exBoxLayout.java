package Layouts;

import java.awt.BorderLayout;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class exBoxLayout {

	public static void main(String[] args) {
		new VentanaBoxLayout();

	}

}

//Apila componentes como si fueran cajas (arriba-abajo / izquierda-derecha)
class VentanaBoxLayout extends JFrame{
	private JPanel panel;
	private JButton[] boton = new JButton[10];
	
	public VentanaBoxLayout(){
		
		panel = new JPanel();
		panel.setLayout(new BoxLayout(panel,BoxLayout.Y_AXIS));
		
		//Instanciamos lista de botones
		for(int i = 0; i< boton.length; i++) {
			boton[i] = new JButton("Boton "+i);
			panel.add(boton[i]);
		}
		
		this.add(panel);
		this.setSize(300,300);
		this.setTitle("Ventana Box Layout");
		this.setVisible(true);
	}
}
