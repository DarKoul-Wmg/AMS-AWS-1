package Layouts;

import java.awt.FlowLayout;

import javax.swing.JFrame;
import javax.swing.JLabel;

public class exFlowLayout{

	public static void main(String[] args) {
		new VentanaFlowLayout();

	}

}

class VentanaFlowLayout extends JFrame{
	
	JLabel etiqueta[] = new JLabel[10];
	public VentanaFlowLayout(){
		
		this.setSize(200,300);
		//JFrame tiene por defecto un BorderLayout
		
		this.setLayout(new FlowLayout(FlowLayout.RIGHT,10,5));
		
		//for para instanciar etiquetas
		for (int i = 0; i<etiqueta.length; i++) {
			etiqueta[i] = new JLabel("Etiqueta "+i, JLabel.CENTER);
			//se inserta en el frame
			this.add(etiqueta[i]);
		}
		
		this.setTitle("Flow Layout");
		//this.pack();
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setVisible(true);
	
	}
	
}