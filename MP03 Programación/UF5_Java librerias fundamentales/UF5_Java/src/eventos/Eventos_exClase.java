package eventos;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;


import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Eventos_exClase {

	public static void main(String[] args) {
		System.out.println("Hola");
		new VentanasEventosV2();

	}
}

class VentanasEventosV2 extends JFrame implements ActionListener{
	
	private JButton boton1,boton2,boton3,boton4;
	private MiPanel2 panelCentral,panel1, panel2; 
	private JLabel etiqueta1;
	
	
	
	VentanasEventosV2(){
		setBounds(400,400,400,400);

		panelCentral = new MiPanel2();		
		panel1 = new MiPanel2();
		panel2 = new MiPanel2();
		
		boton1 = new JButton("Boton1");
		boton2 = new JButton("Boton2");
		boton3 = new JButton("Boton3");
		boton4 = new JButton("Boton4");
		
		etiqueta1 = new JLabel();
		
		getContentPane().setLayout(new BorderLayout());
		panelCentral.setLayout(new BoxLayout(panelCentral,BoxLayout.Y_AXIS));
		
		getContentPane().add(boton1,BorderLayout.WEST);	
		getContentPane().add(boton2,BorderLayout.EAST);
		getContentPane().add(boton3,BorderLayout.NORTH);	
		getContentPane().add(boton4,BorderLayout.SOUTH);
		
		getContentPane().add(panelCentral,BorderLayout.CENTER);
		
		
		//getContentPane().add(panelCentral,BorderLayout.CENTER);	
				
		

		panelCentral.add(panel1);
		panelCentral.add(panel2);
		
		panel1.setBackground(Color.blue);
		panel1.add(etiqueta1);
		etiqueta1.setText("LALA");
		etiqueta1.setForeground(Color.white);//color letra
		panel2.setBackground(Color.green);
		
			
		boton1.addActionListener(this);
		boton2.addActionListener(this);
		
		//boton 3 con action listener
		boton3.addActionListener(this);
		boton4.addActionListener(this);
		
		
		//mouse
		panelCentral.addMouseListener(new EventitosMouse()); //para que aplique lo que hay en la clase adapter
		
		this.setLocationRelativeTo(null);//centra ventana
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
		
	}

	
	public void actionPerformed(ActionEvent e) {
		e.toString();
		
		etiqueta1.setText(e.getActionCommand());
		
		if(e.getSource() == boton1) {
			System.out.println("Hola has clickado el boton1");
			panel1.setBackground(new Color((int)(Math.random()*255),(int)(Math.random()*255),(int)(Math.random()*255)));
		}
		
		if(e.getSource() == boton2) {
			System.out.println("Hola has clickado el boton2");
			panel2.setBackground(new Color((int)(Math.random()*255),(int)(Math.random()*255),(int)(Math.random()*255)));
		}		
	
	}
	
	
	class MiPanel2 extends JPanel implements ActionListener{

		public void actionPerformed(ActionEvent e) {
			if(e.getSource() == boton1) {
				System.out.println("Hola has clickado el boton1");
				panel1.setBackground(new Color((int)(Math.random()*255),(int)(Math.random()*255),(int)(Math.random()*255)));
			}
			if(e.getSource() == boton2) {
				System.out.println("Hola has clickado el boton2");				
				//Color rgb aleatorio
				panel2.setBackground(new Color((int)(Math.random()*255),(int)(Math.random()*255),(int)(Math.random()*255)));
			}
		}
	}
	
	class EventoBoton1 implements ActionListener{
	
			public void actionPerformed(ActionEvent e) {
				System.out.println("Has enviado un objeto del tipo evento a la clase EventoBoton1");
				
			}
		
		}
	
	
	class EventitosMouse extends MouseAdapter{
		public void mouseClicked(MouseEvent e) {
			System.out.println("Has hecho click en el mouse y lo has enviado al adapter");
			
		}
		public void mouseEntered(MouseEvent e) {
			System.out.println("Entras dentro");
			
		}


	
		public void mouseExited(MouseEvent e) {
			System.out.println("Sales fuera");
			
		}
		
	}
	
}
