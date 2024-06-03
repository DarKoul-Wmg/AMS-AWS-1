package paint;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import javax.imageio.ImageIO;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.border.Border;

public class SesionPaint {

	public static void main(String[] args) {
		new VentanaPrevia("Mi titulo");

	}


}

class VentanaPrevia extends JFrame{
	private JPanel panelPrincipal,panelCentral,panel1,panel2;
	private JLabel etiqueta1;
	private JTextArea campoTexto;
	private JButton boton1;
	
	
	VentanaPrevia(String title) {
		setBounds(100,100,400,400);
		setTitle("Hola "+title);
		initComponents();
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	
	public void initComponents() {
		
		panelPrincipal = new JPanel();
		panelCentral = new JPanel();
		panel1 = new JPanel();
		panel2 = new JPanel();
		
		etiqueta1 = new JLabel("etiqueta");
		campoTexto = new JTextArea("Text Area");
		boton1 = new JButton("Boton1");
		
		add(panelPrincipal);
		panelPrincipal.setLayout(new BorderLayout());
		panelPrincipal.add(panelCentral,BorderLayout.CENTER);
		
		panelCentral.setBackground(Color.YELLOW);
		panelCentral.setLayout(new BoxLayout(panelCentral, BoxLayout.Y_AXIS));
		
		panel1.setLayout(new BoxLayout(panel1, BoxLayout.X_AXIS));
		panel1.add(etiqueta1);
		panel1.add(campoTexto);
		panel1.setBackground(Color.RED);
		
		panel2.add(boton1);
		panelCentral.add(panel1);
		panelCentral.add(boton1);
		panelCentral.add(panel2);
		
		boton1.addActionListener(new ActionListener() { //Se crea una clase al vuelo
			
			public void actionPerformed(ActionEvent e) {
				new MiVentana0(campoTexto.getText());
				
				dispose();				
			}
		});
	
	}
}

class MiPanelito extends JPanel{ //esto es un JPanel, sirve para añadir funcionalidad adicional ()
	
	private int numeroPanel;
	private BufferedImage imagen;
	
	public int getNumeroPanel(){
		return numeroPanel;
	}
	
	public void setNumeroPanel(int numeroPanel){
		this.numeroPanel = numeroPanel;
	}
	
	
	
	//tiene este metodo implementado al ser un JPanel
	
	public void paint(Graphics g) {
		super.paint(g);
		
		////imagen en el pain
		g.drawImage(imagen, 0, 0, this.getWidth(), this.getHeight(), null);
		//g.fillOval(0, 0, 30, 30);
	}
	
	
	//set get Buffimage
	public BufferedImage getImagen() {
		return imagen;
	}

	public void setImagen(BufferedImage imagen) {
		this.imagen = imagen;
	}
	
}

class MiVentana0 extends JFrame{
	
	private MiPanelito panelPrincipal,panelCentral, panelOeste, panelSur;
	private JButton boton1,boton2;
	private ArrayList<BufferedImage> imagenes;
	private JLabel etiquetaTexto;
	
	MiVentana0(String title) {
		setBounds(100,100,400,400);
		setTitle("Hola "+title);
		initComponents();
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	
	public void initComponents() {
		imagenes = new ArrayList<BufferedImage>();
		
		for (int i=1;i<=9;i++) {
			try {
				imagenes.add(ImageIO.read(new File("./src/paint/Imagen"+i+".JPG")));
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		
		panelPrincipal = new MiPanelito();
		panelCentral = new MiPanelito();
		panelOeste = new MiPanelito();
		
		add(panelPrincipal);
		panelPrincipal.setBackground(Color.blue);
		panelPrincipal.setLayout(new BorderLayout());
		panelPrincipal.add(panelCentral,BorderLayout.CENTER);
		panelPrincipal.add(panelOeste,BorderLayout.WEST);
		
		boton1 = new JButton("Boton1");
		boton2 = new JButton("Boton2");
		
		panelOeste.setLayout(new BoxLayout(panelOeste, BoxLayout.Y_AXIS));
		panelOeste.add(boton1);
		panelOeste.add(boton2);
		boton1.addActionListener(new ActionListener() {
			
			
			public void actionPerformed(ActionEvent e) {
				
				int numero = (int) (Math.random()*9);
				panelCentral.setImagen(imagenes.get(numero));
				panelCentral.setNumeroPanel(numero);
				etiquetaTexto.setText("La imagen es la: "+ numero);
				System.out.println(numero);
				panelCentral.repaint();
				
			}
		});
		
		boton2.addActionListener(new ActionListener() {
			
			
			public void actionPerformed(ActionEvent e) {
				
				Graphics g = panelPrincipal.getGraphics();			

				g.fillRect(20, 20, 30, 30);
				
			}
		});
		
		panelSur = new MiPanelito();
		etiquetaTexto = new JLabel("Texto en la etiqueta");
		panelSur.add(etiquetaTexto);
		
		panelPrincipal.add(panelSur,BorderLayout.SOUTH);
		
		panelCentral.addMouseListener(new EventosPanelCentralMouseClicked() );
		////panel principal genera eventos y van a ser recogidos por esa clase
		//panelPrincipal.addMouseMotionListener(new EventosPanelPrincipalMouseMotion() );
		//panelPrincipal.addMouseMotionListener(new EventosPanelPrincipalMouseMotion() );
		
		
		try { //OBLIGA PONERLO
			//panelPrincipal.setImagen(ImageIO.read(new File("./src/paint/Imagen2.JPG")));
			panelCentral.setImagen(ImageIO.read(new File("./src/paint/Imagen2.JPG")));
		} catch (IOException e) {
			
			e.printStackTrace();
		}
		
		//panelPrincipal.addMouseListener(new EventosPanelPrincipalMouseClicked());
		
		
	}
	
	class EventosPanelPrincipalMouseMotion implements MouseMotionListener{

		public void mouseDragged(MouseEvent e) { //evento generado por el panel principal
			
			System.out.println("mouseDragged = "+e.getButton());
			if(e.getButton() == 0) {
				int posX = e.getX();
				int posY = e.getY();
				
				Graphics g = panelPrincipal.getGraphics();			
				//panelPrincipal.repaint();
				//coordenadas relativas al panelPrincipal (donde se recogen los graficos)
				g.fillRect(posX, posY, 30, 30);
			}
			
		}

	
		public void mouseMoved(MouseEvent e) {
				
		}
	}
	
	class EventosPanelCentralMouseClicked implements MouseListener{

		
		public void mouseClicked(MouseEvent e) {
//			System.out.println("mouseClicked = "+e.getButton());
//			if (e.getButton() == 3) {
//				panelPrincipal.repaint();
//			}
			int numero = (int) (Math.random()*9);
			panelCentral.setImagen(imagenes.get(numero));
			panelCentral.setNumeroPanel(numero);
			System.out.println(numero);
			panelCentral.repaint(); //Cada vez que hago repaint llamo al metodo paint para poder redibujar la imagen nueva obtenida con cada click
			
		}

	
		public void mousePressed(MouseEvent e) {
			
			
		}

	
		public void mouseReleased(MouseEvent e) {
			
			
		}


		public void mouseEntered(MouseEvent e) {
			
			
		}

	
		public void mouseExited(MouseEvent e) {
			
			
		}

		
	}
	
}