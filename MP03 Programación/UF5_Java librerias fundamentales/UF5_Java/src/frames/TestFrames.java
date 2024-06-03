package frames;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class TestFrames {

	public static void main(String[] args) {
		Ventana v = new Ventana();
		

	}}
	
class Ventana extends JFrame{
	BufferedImage image; // Declaramos una buffered image
	
	JPanel panelPrincipal,panelLateral1; //Panel
	
	JButton boton1,boton2,boton3,boton4,boton5;
	
	Ventana(){
//		setSize(400, 300); // Tamano de ventana
//		setLocation(200,200); // Desplaza la ventana emergente
		
		super("MIS PRIMERAS VENTANAS"); // Si NO esta setTitle, pone el titulo de dentro 
		setBounds(200, 200, 400, 300); // Fusion de los metodos setSize y setLocations		
		setTitle("Mis primeras ventanas"); //Titulo de la ventana
		
//		setResizable(false); // Capacidad de reescalar la ventana
		
		try {
			
			image = ImageIO.read(new File ("./src/frames/pent_icon_1.png")); // Sacamos la imagen del directorio
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		setIconImage(image);// cambia la imagen del icono de la ventana
		
		panelPrincipal = new JPanel(); //Iniciamos el panel
		panelLateral1 = new JPanel();
		add(panelPrincipal);
		
		panelPrincipal.setLayout(new BorderLayout()); // Creamos un layout para editar la disposicion de los botones
//		panelPrincipal.setLayout(new FlowLayout()); // Layout por defecto, disposicion automatica
//		panelPrincipal.setLayout(new BoxLayout(panelPrincipal,BoxLayout.Y_AXIS)); // Desplega en el eje correspondeinte  de los botones
																				  // Espacio en vertical Y u horizontal X.
		
		panelPrincipal.setBackground(Color.black); //cambiar el color del panel
		
		
		//Anadir los botones al panel
		
		boton1 = new JButton("b1");
		boton2 = new JButton("b2");
		boton3 = new JButton("b3");
		boton4 = new JButton("b4");
		boton5 = new JButton("b5");
//		panelPrincipal.add(boton1); 
//		panelPrincipal.add(boton2);
//		panelPrincipal.add(boton3);
//		panelPrincipal.add(boton4);
//		panelPrincipal.add(boton5);
//		panelPrincipal.add(boton1,BorderLayout.NORTH); // Ocupa toda la area de la zona indicada del layout
//		panelPrincipal.add(boton2,BorderLayout.SOUTH);
//		panelPrincipal.add(boton3,BorderLayout.WEST);
//		panelPrincipal.add(boton4,BorderLayout.EAST);
//		panelPrincipal.add(boton5,BorderLayout.CENTER);
		
		
		//Anadir panel a un panel:
		panelPrincipal.add(panelLateral1,BorderLayout.NORTH);
		panelLateral1.setBackground(Color.RED);
		panelLateral1.setLayout(new BoxLayout(panelLateral1, BoxLayout.X_AXIS));
		panelLateral1.add(boton1);
		panelLateral1.add(boton2);
		panelLateral1.add(boton3);

		
		
		
		
		setDefaultCloseOperation(EXIT_ON_CLOSE); // Cierra automaticamente la ejecución en segundo plano de la ventana cuando se cierra
		setVisible(true);//Ventanas por defecto son invisibles
	}}

