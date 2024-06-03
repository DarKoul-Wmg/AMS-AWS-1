package paint;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionAdapter;
import java.awt.event.MouseMotionListener;

import javax.swing.JButton;
import javax.swing.JFrame;

public class EjemploGraphicsEventos {
	
	private JFrame marco;
	private JButton esborrar;
	
	public EjemploGraphicsEventos() {
		marco = new JFrame();
		esborrar = new JButton("Limpiar pantalla");
		
		//dibujar en el marco con el cursor
		marco.addMouseMotionListener(new MouseMotionAdapter() {  //Al hacer mouse Adapter, solo ponemos los que vamos a necesitar
			
			public void mouseMoved(MouseEvent e) {
				// sacamos posiciones del raton para poder dibujar:
				int x = e.getX();
				int y = e.getY();
				
				Graphics g = marco.getGraphics();
				g.setColor(Color.red);
				g.fillOval(x-3, y-3, 6, 6);
				
			}

		});
		
		esborrar.addActionListener(new ActionListener() { //Solo existe adapter si tiene mas de un metodo, en este caso solo hay uno
			
			public void actionPerformed(ActionEvent e) {
				marco.repaint();
				
			}
		});
		
		
		marco.add(esborrar,BorderLayout.SOUTH);
		marco.setSize(300,200);
		marco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		marco.setVisible(true);
		marco.setLocationRelativeTo(null);
	}

	public static void main(String[] args) {
		new EjemploGraphicsEventos();

	}

}
