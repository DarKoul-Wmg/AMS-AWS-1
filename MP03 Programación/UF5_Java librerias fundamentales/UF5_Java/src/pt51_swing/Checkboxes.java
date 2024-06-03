package pt51_swing;


import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.*;


public class Checkboxes {
	
	public static void main(String[] args) {
	
		new VentanaEx1();
	}

}

class VentanaEx1 extends JFrame{
	private JPanel panelPrincipal,panelCentral,panel1,panel2;
	private JCheckBox color,negreta,inclinada,gran;
	private JLabel etiqueta;
	private BufferedImage image;

	
	public VentanaEx1(){
		
		setBounds(200,200,500,200);
		setTitle("ex1 pt51 Checkbox");
		initComponents();
		
		try {
			
			image = ImageIO.read(new File ("./src/pt51_swing/pent_icon_1.png")); // Sacamos la imagen del directorio
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		setIconImage(image);
		
		setResizable(false);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	
	public void initComponents() {
		
		panelPrincipal = new JPanel();
		panelPrincipal.setLayout(new BorderLayout());
		
		panelCentral = new JPanel();
		panelCentral.setLayout(new FlowLayout(FlowLayout.CENTER)); // Ajustamos valores para que solo haya una fila y dos columnas (los paneles)
		
		add(panelPrincipal);
		panel1 = new JPanel();
		panel1.setLayout(new BorderLayout());
		
		
		panel2 = new JPanel();
		panel2.setLayout(new BoxLayout(panel2,BoxLayout.Y_AXIS));
		
		color = new JCheckBox("Color",false);
		negreta = new JCheckBox("Negreta",false);
		inclinada = new JCheckBox("Inclinada",false);
		gran = new JCheckBox("Gran",false);
		
		etiqueta = new JLabel("Juguem amb CheckBoxes....");
		etiqueta.setFont(new Font("Arial", Font.PLAIN, 30));
		//anadimos campos checkbox
		panel2.add(color);
		panel2.add(negreta);
		panel2.add(inclinada);
		panel2.add(gran);
		panel1.add(etiqueta,BorderLayout.CENTER);
		
		panelCentral.add(panel1);
		panelCentral.add(panel2);
		panelPrincipal.add(panelCentral);
		
		
	}
}

