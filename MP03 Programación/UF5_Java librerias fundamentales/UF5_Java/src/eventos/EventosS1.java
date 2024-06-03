package eventos;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class EventosS1 {

	public static void main(String[] args) {
		System.out.println("Hola");
		new VentanasEventos();

	}

}

class VentanasEventos extends JFrame implements ActionListener{ //Hacemos que pueda usar ActionListener
	
	private JButton boton1,boton2;
	private MiPanel panelCentral; //clase creada abajo
	
	
	VentanasEventos(){
		setBounds(400,400,400,400);
		
		//Trae un panel por defecto
//		panelDelFrame = (JPanel) getContentPane();
		panelCentral = new MiPanel();
		
		boton1 = new JButton("Boton1");
		boton2 = new JButton("Boton2");
		add(boton1,BorderLayout.WEST);	
		add(boton2,BorderLayout.EAST);
		
		//getContentPane().setBackground(Color.black);
		
		getContentPane().add(panelCentral,BorderLayout.CENTER);
		panelCentral.setBackground(Color.yellow);
		
		
		
		//Anadir acciones a los botones:
		boton1.addActionListener(panelCentral); //Aqui pasa el objeto al panel de la otra clase
		
		boton2.addActionListener(this);//indica quien recibe el objeto (en este caso él mismo) 
		   //(hay que habilitar a la clase para que reciba el objeto)
		
		this.setLocationRelativeTo(null);//centra ventana
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
		
	}

	//Esto indica a quien se le pasa el objeto Evento creado (es un implemented metod)
	public void actionPerformed(ActionEvent e) {
		
		e.toString();// El objeto obtenido tambien tiene metodos
		if(e.getSource() == boton1) {
			System.out.println("Hola has clickado el boton1");
		}
		
		if(e.getSource() == boton2) {
			System.out.println("Hola has clickado el boton2");
			panelCentral.setBackground(Color.black);
		}
		//System.out.println(e.toString());
	}
	
	
	
	//Creamos clase interna para acceder a los atributos internos de la propia clase  
	class MiPanel extends JPanel implements ActionListener{
		//usar geters
		
		public void actionPerformed(ActionEvent e) {
			if(e.getSource() == boton1) {
				System.out.println("Hola has clickado el boton1");
				
				//Color rgb aleatorio
				setBackground(new Color((int)(Math.random()*255),(int)(Math.random()*255),(int)(Math.random()*255)));
			}
		}
	}
}
