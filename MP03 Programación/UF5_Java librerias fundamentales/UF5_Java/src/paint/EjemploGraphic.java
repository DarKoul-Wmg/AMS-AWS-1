package paint;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Toolkit;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class EjemploGraphic extends JFrame{
	private JPanel panel;
	
	
	public EjemploGraphic() {
		initFrame();
		initPanel();
	}
	
	
	private void initFrame() {
		setTitle("Ejemplo Graficos 1");
		setSize(800,600);
		setResizable(false);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
		
	}
	
	private void initPanel() {
		panel = new JPanel(); //inicio panel
		add(panel); //agregado al frame
		panel.setPreferredSize(new Dimension(800,600)); //dimensiones panel
	}

		
	public void paint(Graphics g) {
		super.paint(g);
		Graphics2D g2d = (Graphics2D)g;
		
		//Linea
		g2d.setColor(Color.BLUE);
		
		g2d.setStroke(new BasicStroke(5));
		g2d.drawLine(30, 70, 770, 70);
		
		
		//Rectangulo (rellendo y borde)
		
		g2d.fillRect(30, 100, 350, 60); //relleno
		g2d.setColor(Color.black);
		g2d.drawRect(30, 100, 350, 60); //borde
		
		//Rectangulo redondeado
		g2d.setColor(Color.CYAN);
		g2d.drawRoundRect(420, 100, 350, 60, 10, 10);
		
		//Arco
		g2d.setColor(Color.PINK);
		g2d.drawArc(30, 200, 100, 100, 180, -90);
		
		//Circulo
		g2d.setColor(Color.RED);
		g2d.drawOval(100, 200, 100, 100);
		
		//Ovalo (con relleno y borde)
		g2d.setColor(Color.YELLOW);
		g2d.fillOval(240, 200, 150, 100);
		g2d.setColor(Color.BLACK);
		g2d.drawOval(240, 200, 150, 100);
		
		
		//Poligono (5 lados con relleno y borde)
		int [] pentagono_x = {670,650,700,750,730};
		int [] pentagono_y = {300,245,200,245,300};
		g2d.setColor(Color.MAGENTA);
		g2d.fillPolygon(pentagono_x, pentagono_y, 5);
		g2d.setColor(Color.BLACK);
		g2d.drawPolygon(pentagono_x, pentagono_y, 5);
		
		//Texto		
		g2d.setFont(new Font("ARIAL", Font.PLAIN, 32));
		g2d.drawString("HOLA MON", 30, 400);
		
		//Imagen
		Toolkit t = Toolkit.getDefaultToolkit();
		Image imagen = t.getImage("./src/paint/Imagen7.JPG");
		g2d.drawImage(imagen, 300, 325, this);
		
		
		//Degradado
		GradientPaint gp = new GradientPaint(400, 350, Color.RED, 770, 350,Color.GREEN);
		g2d.setPaint(gp);
		g2d.fillRect(400, 350, 370, 200);
	}
	
	
	public static void main(String[] args) {
		
		new EjemploGraphic();
	}

}
