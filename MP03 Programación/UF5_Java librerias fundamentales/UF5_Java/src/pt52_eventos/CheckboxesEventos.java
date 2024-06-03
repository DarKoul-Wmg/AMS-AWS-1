package pt52_eventos;


import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.*;


public class CheckboxesEventos {
	
	public static void main(String[] args) {
	
		new Ventana51Ex1();
	}

}

class Ventana51Ex1 extends JFrame{
	private JPanel panelPrincipal,panelCentral,panel1,panel2;
	private JCheckBox color,negreta,inclinada,gran;
	private JLabel etiqueta;
	private BufferedImage image;

	
	public Ventana51Ex1(){
		
		setBounds(200,200,500,200);
		setTitle("ex1 pt52 CheckboxEvents");
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
		color.addActionListener(new ActionListener() {
			//clase vulelo para cambiar el color
			public void actionPerformed(ActionEvent e) {
				
				if (e.getSource() == color && color.isSelected()) {
	                panel1.setBackground(Color.magenta);
	                etiqueta.setBackground(Color.magenta);
	                
	            } else if (e.getSource() == color && !color.isSelected()) {
	            	etiqueta.setBackground(null);
	                panel1.setBackground(null);
	            }
			}
		});
		
		negreta = new JCheckBox("Negreta",false);
		negreta.addActionListener(new EventosCheckBox());
		
		inclinada = new JCheckBox("Inclinada",false);
		inclinada.addActionListener(new EventosCheckBox());
		
		gran = new JCheckBox("Gran",false);
		gran.addActionListener(new EventosCheckBox());
		
		etiqueta = new JLabel("Juguem amb CheckBoxes....");
		etiqueta.setFont(new Font("Arial", Font.PLAIN, 20));
		etiqueta.setOpaque(true);
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
	class EventosCheckBox implements ActionListener{
		public void actionPerformed(ActionEvent e) {
			//acciones segun checkbox activa en la letra
			
            if (e.getSource() == negreta && negreta.isSelected()) {
                etiqueta.setFont(etiqueta.getFont().deriveFont(Font.BOLD));
                
            } else if (e.getSource() == negreta && !negreta.isSelected()) {
                etiqueta.setFont(etiqueta.getFont().deriveFont(Font.PLAIN));
            }
            
            if (e.getSource() == inclinada && inclinada.isSelected()) {
                etiqueta.setFont(etiqueta.getFont().deriveFont(Font.ITALIC));
                
            } else if (e.getSource() == inclinada && !inclinada.isSelected()) {
                etiqueta.setFont(etiqueta.getFont().deriveFont(Font.PLAIN));
            }
            
            if (e.getSource() == gran && gran.isSelected()) {
                etiqueta.setFont(etiqueta.getFont().deriveFont(40f));
            } else if (e.getSource() == gran && !gran.isSelected()) {
                etiqueta.setFont(etiqueta.getFont().deriveFont(20f));
            }
		
		}
  }
}


