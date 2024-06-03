package pt_Extra;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Timer;

import javax.imageio.ImageIO;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;





public class MemoryImagenes {
	public static void main(String[] args) {
		new VentanaPrevia("Memory ");

	}
}

class VentanaPrevia extends JFrame{
	private MiPanelito panelPrincipal,panelCentral,panel1,panel2,panelImagen;
	private JLabel etiqueta1;
	private JTextArea campoTexto;
	private JButton boton1, boton2;
	private ArrayList<BufferedImage> imagenes;
	
	
	VentanaPrevia(String title) {
		setBounds(100,100,400,400);
		setTitle(title);
		initComponents();
		
		setLocationRelativeTo(null);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	

	public void initComponents() {
	
		imagenes = new ArrayList<BufferedImage>();
			
		for (int i=1;i<=9;i++) {
			try {
				imagenes.add(ImageIO.read(new File("./src/paint/Imagen"+i+".JPG")));
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		panelPrincipal = new MiPanelito();
		panelCentral = new MiPanelito();
		panel1 = new MiPanelito();
		panel2 = new MiPanelito();
		panelImagen = new MiPanelito();
		
		etiqueta1 = new JLabel("Ingresa el nombre del jugador: ");
		campoTexto = new JTextArea("nombre...");
		boton1 = new JButton("Entrar");
		boton2 = new JButton("Salir");
		
		add(panelPrincipal);
		panelPrincipal.setLayout(new BorderLayout());
		panelPrincipal.add(panelCentral,BorderLayout.CENTER);
		
//		panelCentral.setBackground(Color.YELLOW);
		panelCentral.setLayout(new BorderLayout());
		
		panel1.setLayout(new BoxLayout(panel1, BoxLayout.X_AXIS));
		panel1.add(etiqueta1);
		panel1.add(campoTexto);
		panel1.setBackground(Color.RED);
		panelCentral.add(panel1, BorderLayout.NORTH);
		
		panel2.add(boton1);
		panel2.add(boton2);
		panelCentral.add(panel2, BorderLayout.SOUTH);
		
		panelCentral.add(panelImagen,BorderLayout.CENTER);
		
		panelImagen.addMouseListener(new EventosPanelImagen());
		

		boton1.addActionListener(new ActionListener() { //Se crea una clase al vuelo
			
			public void actionPerformed(ActionEvent e) {
				new MiVentanaMemory(campoTexto.getText());
				
				dispose();				
			}
		});
		
		boton2.addActionListener(new ActionListener() { //Se crea una clase al vuelo
				
				public void actionPerformed(ActionEvent e) {
					
					dispose(); //ciera ventana actual	
					System.exit(0);
			}
		});
	}
	
	//Al pulsar el panel
	class EventosPanelImagen extends MouseAdapter{  //PARA MOUSEADAPTER ES extends

	
		public void mouseClicked(MouseEvent e) {
			int numero = (int)(Math.random()*9);
			panelImagen.setImagen(imagenes.get(numero));
			System.out.println("Estas viendo la imagen: "+numero);
			panelImagen.repaint();
			
		}	
	}
	
}
class MiPanelito extends JPanel{ //esto es un JPanel, sirve para añadir funcionalidad adicional ()
 

	private BufferedImage imagen;
	private boolean visible = false;

	
	//tiene este metodo implementado al ser un JPanel
	
	public void paint(Graphics g) {
		super.paint(g);
		
		if (visible && imagen != null) {  // Solo dibujar la imagen si está visible y si es una imagen valida
            g.drawImage(imagen, 0, 0, this.getWidth() - 10, this.getHeight() - 10, null);
        }
	}
	
	//set get Buffimage
	public BufferedImage getImagen() {
		return imagen;
	}

	public void setImagen(BufferedImage imagen) {
		this.imagen = imagen;
	}
	
	//metodos para estados del panel
	public void ocultarImagenPanel(){
		visible = false;
		repaint();
	}
	public void mostrarImagenPanel() {
		visible = true;
		repaint();
	}
	
	
	public boolean getVisible(){
		return visible; 
	}
}

class MiVentanaMemory extends JFrame{
	
	private MiPanelito panelPrincipal;
	private JButton botonS;
	private ArrayList<BufferedImage> imagenes, imagenesMemory;
	private JLabel tablerosResueltos;
	private MiPanelito panelOrigen[][];

	//variables para guardar los dos paneles seleccionadops
    private int primerPanelSeleccionado = -1;
    private int segundoPanelSeleccionado = -1;
    
    private int puntos = 0;
    
	
	MiVentanaMemory(String title) {
		setBounds(100,100,400,400);
		setTitle("Hola "+title);
		initComponents();
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
		setLocationRelativeTo(null);
	}
	
	public void initComponents() {
		panelOrigen = new MiPanelito[3][3];
		
		panelPrincipal = new MiPanelito();
		panelPrincipal.setLayout(new GridLayout(3,3));
		add(panelPrincipal, BorderLayout.CENTER);	
		
		imagenesMemory = new ArrayList<BufferedImage>();
		imagenes = new ArrayList<BufferedImage>();
		
		Random random = new Random();
		
		//genera todas las imagenes disponibles
		for (int i=1;i<=9;i++) {
			try {
				imagenes.add(ImageIO.read(new File("./src/paint/Imagen"+i+".JPG")));
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		//Rellenar la lista de imagenes que van a ser anadidas al tablero: imagenesMemory
		
				//clonamos la lista para iterar sobre ella y evitar repetidos
		ArrayList<BufferedImage> imagenesDisponibles = new ArrayList<>(imagenes);
		
		while(imagenesMemory.size() < 8) { //numero aleatorio en funcion del tamano de la arraylist
			int indiceAleatorio = random.nextInt(imagenesDisponibles.size());
			BufferedImage imagenAleatoria = imagenesDisponibles.get(indiceAleatorio);
			imagenesMemory.add(imagenAleatoria);
			imagenesMemory.add(imagenAleatoria);
			imagenesDisponibles.remove(indiceAleatorio);

		}
	
		// rellenar tablero de paneles con las imagenes
		int index = 0;
		for(int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				
				if( i==1 && j==1) {
					 panelOrigen[i][j] = new MiPanelito();
	                 panelOrigen[i][j].setImagen(null); // panel central en blanco
					
				}else {
					panelOrigen[i][j] = new MiPanelito();
					panelOrigen[i][j].setBackground(Color.gray);
					panelOrigen[i][j].setImagen(imagenesMemory.get(index));
					panelOrigen[i][j].addMouseListener(new EventosPanelImagen(i,j,panelOrigen[i][j]));
					index++;
				}
				panelPrincipal.add(panelOrigen[i][j]);
			}
		}
	}
	
	//Clase apra los eventos de raton
	
	private class EventosPanelImagen extends MouseAdapter{
		private int fila,columna;
		private MiPanelito panel;
		
		public EventosPanelImagen(int fila, int columna, MiPanelito panel) {
			this.fila = fila;
			this.columna = columna;
			this.panel = panel;
		}
		
		public void mouseClicked(MouseEvent e) {
	        // Si el panel está oculto, lo hacemos visible
	        if (!panel.getVisible()) {
	            panel.mostrarImagenPanel();
	            
	        } else {
	            // Si ya está visible, comprobamos si hay dos paneles visibles para comparar
	            if (primerPanelSeleccionado == -1) {
	                // No hay paneles previamente seleccionados, marcamos este como primer panel
	                primerPanelSeleccionado = fila * 3 + columna;
	            } else {
	                // Ya hay un panel visible, comparamos con el panel actual
	                segundoPanelSeleccionado = fila * 3 + columna;
	                comprobarPares();
	            }
	        }
	    }
	}
	private void comprobarPares() {
	    MiPanelito primerPanel = panelOrigen[primerPanelSeleccionado / 3][primerPanelSeleccionado % 3];
	    MiPanelito segundoPanel = panelOrigen[segundoPanelSeleccionado / 3][segundoPanelSeleccionado % 3];

	    if (primerPanel.getVisible() && segundoPanel.getVisible()) {
	        BufferedImage imgPrimerPanel = primerPanel.getImagen();
	        BufferedImage imgSegundoPanel = segundoPanel.getImagen();

	        if (imgPrimerPanel.equals(imgSegundoPanel)) {
	            puntos++;
	            System.out.println("¡Encontraste un par! Puntaje: " + puntos);
	        } else {
	            System.out.println("¡Intenta de nuevo!");
	            panelOrigen[primerPanelSeleccionado / 3][primerPanelSeleccionado % 3].ocultarImagenPanel();
	            panelOrigen[segundoPanelSeleccionado / 3][segundoPanelSeleccionado % 3].ocultarImagenPanel();
	        }

	        // Reiniciar paneles seleccionados
	        primerPanelSeleccionado = -1;
	        segundoPanelSeleccionado = -1;

	        if (puntos == 4) {
	            System.out.println("¡Felicidades, has ganado!");
	            dispose();
	        }
	    }
	}

}