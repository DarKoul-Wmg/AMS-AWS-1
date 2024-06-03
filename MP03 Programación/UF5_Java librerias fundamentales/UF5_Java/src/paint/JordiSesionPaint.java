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

public class JordiSesionPaint {

	public static void main(String[] args) {
		new MiVentana0("Mi titulo");
		//new VentanaPrevia();

	}

}
class VentanaPreviaJ extends JFrame{
	JPanel panelPrincipal,panelCentral,panel1,panel2;
	JLabel etiqueta1;
	JTextArea campoTexto;
	JButton boton1;
	VentanaPreviaJ(){
		setBounds(100, 100, 400, 400);
		initComponents();
		
	
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	public void initComponents() {
		panelPrincipal = new JPanel();
		panelCentral = new JPanel();
		panel1 = new JPanel();
		panel2 = new JPanel();
		etiqueta1 = new JLabel("Etiqueta");
		campoTexto = new JTextArea("TestArea");
		boton1 = new JButton("Boton1");
		add(panelPrincipal);
		panelPrincipal.setLayout(new BorderLayout());
		panelPrincipal.add(panelCentral,BorderLayout.CENTER);
		
		panelCentral.setLayout(new BoxLayout(panelCentral, BoxLayout.Y_AXIS));
		panelCentral.setBackground(Color.YELLOW);
		
		panel1.setLayout(new BoxLayout(panel1, BoxLayout.X_AXIS));
		panel1.add(etiqueta1);
		panel1.add(campoTexto);
		panelCentral.add(panel1);
		panel1.setBackground(Color.RED);
		
		panelCentral.add(panel2);
		panel2.add(boton1);
		
		boton1.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent arg0) {
				new MiVentana0(campoTexto.getText());
				dispose();
			}
		});
	}
	
}
class MiPanelitoJ extends JPanel{
	int numeroPanel;
	BufferedImage imagen;

	public int getNumeroPanel() {
		return numeroPanel;
	}

	public void setNumeroPanel(int numeroPanel) {
		this.numeroPanel = numeroPanel;
	}
	

	public BufferedImage getImagen() {
		return imagen;
	}

	public void setImagen(BufferedImage imagen) {
		this.imagen = imagen;
	}

	public void paint(Graphics arg0) {
		super.paint(arg0);
		arg0.drawImage(imagen, 0, 0, this.getWidth(), this.getHeight(), null);
		//arg0.fillOval(0, 0, 30, 30);
		
	}

	
}
class MiVentana0J extends JFrame{
	int puntos;
	MiPanelitoJ panelPrincipal,panelCentral,panelOeste,panelSur;
	JButton boton1,boton2;
	ArrayList<BufferedImage> imagenes;
	JLabel etiquetaTexto;
	
	MiVentana0J(String title){
		setBounds(100, 100, 400, 400);
		setTitle("Hola "+title);
		initComponents();
		
	
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	public void initComponents() {
		boton1 = new JButton("Boton1");
		boton2 = new JButton("Boton2");
		imagenes = new ArrayList<BufferedImage>();
		for (int i=1;i<=9;i++) {
			try {
				imagenes.add(ImageIO.read(new File("./src/paint/Imagen"+i+".JPG")));
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		panelPrincipal = new MiPanelitoJ();
		panelCentral = new MiPanelitoJ();
		panelOeste  = new MiPanelitoJ();
		add(panelPrincipal);
		panelPrincipal.setBackground(Color.BLUE);
		panelPrincipal.setLayout(new BorderLayout());
		panelPrincipal.add(panelCentral,BorderLayout.CENTER);
		panelPrincipal.add(panelOeste,BorderLayout.WEST);
		panelOeste.setLayout(new BoxLayout(panelOeste, BoxLayout.Y_AXIS));
		panelOeste.add(boton1);
		panelOeste.add(boton2);
		boton1.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent arg0) {
				int numero = (int) (Math.random()*9 );
				panelCentral.setImagen(imagenes.get(numero));
				panelCentral.setNumeroPanel(numero);
				etiquetaTexto.setText("Tenemos imagen "+numero);
				panelCentral.repaint();
				
			}
		} );
		
		boton2.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent arg0) {

				Graphics g = panelCentral.getGraphics();

				g.fillRect(20, 20, 30, 30);
			}
		});
		panelSur = new MiPanelitoJ();
		etiquetaTexto = new JLabel("Texto en la etiqueta ");
		panelSur.add(etiquetaTexto);
		panelPrincipal.add(panelSur,BorderLayout.SOUTH);
		
		panelCentral.addMouseListener(new EventosPanelCentralMouseClicked());
		//panelPrincipal.addMouseMotionListener(new EventosPanelPrincipalMouseMotion() );
		//panelPrincipal.addMouseListener(new EventosPanelPrincipalMouseClicked());
//		try {
//			panelPrincipal.setImagen(ImageIO.read(new File("./src/Imagen2.JPG")));
//		} catch (IOException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
	}
//	class EventosPanelCentralMouseClicked implements MouseMotionListener{
//
//		public void mouseDragged(MouseEvent arg0) {
//			System.out.println("mouseDragged = "+arg0.getButton());
//			if (arg0.getButton() == 0) {
//				int posX = arg0.getX();
//				int posY = arg0.getY();
//				Graphics g = panelCentral.getGraphics();
//				//panelPrincipal.repaint();
//
//				g.fillRect(posX, posY, 30, 30);
//			}
//
//			
//			
//		}
//
//
//		public void mouseMoved(MouseEvent arg0) {
//			// TODO Auto-generated method stub
//			
//		}
//		
//	}
	
	class EventosPanelCentralMouseClicked implements MouseListener{

		
		public void mouseClicked(MouseEvent arg0) {
//			System.out.println("mouseClicked = "+arg0.getButton());
//			if (arg0.getButton() == 3) {
//				panelPrincipal.repaint();
//			}
			int numero = (int) (Math.random()*9 );
			panelCentral.setImagen(imagenes.get(numero));
			panelCentral.setNumeroPanel(numero);
			System.out.println(numero);
			panelCentral.repaint();
			
		}

		@Override
		public void mouseEntered(MouseEvent arg0) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseExited(MouseEvent arg0) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mousePressed(MouseEvent arg0) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void mouseReleased(MouseEvent arg0) {
			// TODO Auto-generated method stub
			
		}
		
	}
}