package eventos;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

public class VentanaEventos {

	public static void main(String[] args) {
		new Ventana1();

	}

}
class Ventana1 extends JFrame{
	private JPanel panel1,panel2;
	private JButton botonRojo,botonVerde;
	private JLabel contrasena,nom,avis;
	private JTextField jtTexto;
	private JPasswordField password;
	
	public Ventana1() {
		
		this.setSize(300,180);
		this.setTitle("Varios Eventos");
		panel1 = new JPanel();
		panel1.setLayout(new GridLayout(2,2));
		panel2 = new JPanel();
		password = new JPasswordField(10);
		nom = new JLabel("NOM: ");
		jtTexto = new JTextField(10);
		contrasena = new JLabel("CONTRASENA: ");
		avis = new JLabel("La contrasena: Entre 8 y 10 caracteres");
		
		password.addFocusListener(new FocusListener() {

		
			public void focusGained(FocusEvent e) { //cuando el usario entra al cuadr de texto, aparece
				avis.setVisible(true);
				
			}

		
			public void focusLost(FocusEvent e) {
				avis.setVisible(false);
				
			}
			
		});
		
		panel1.add(nom);
		panel1.add(jtTexto);
		panel1.add(contrasena);
		panel1.add(password);
		avis.setVisible(false); //Solo visible cuando gane el foco el cuadro de texto para instroducir contra
		
		botonRojo = new JButton("Color Rojo");
		botonVerde = new JButton("Color Verde");
		
		botonRojo.addActionListener(new PintarColor());
		botonVerde.addActionListener(new PintarColor());
		
		panel2.add(botonRojo);
		panel2.add(botonVerde);
		this.add(panel1,BorderLayout.NORTH);
		this.add(avis,BorderLayout.CENTER);
		this.add(panel2, BorderLayout.SOUTH);
		
		this.setResizable(false);
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
		
	}
	//creamos clase interna porque lo implementan dos componenrtes
	class PintarColor implements ActionListener{
		
		public void actionPerformed(ActionEvent e) {
			
			//JButton b = (JButton) e.getSource();
			
			if (e.getActionCommand().equals("Color Rojo")) {
				panel1.setBackground(Color.RED);
				
			}else if (e.getActionCommand().equals("Color Verde")) {
				panel1.setBackground(Color.GREEN);
			}
			
		}
	}
}
		
	