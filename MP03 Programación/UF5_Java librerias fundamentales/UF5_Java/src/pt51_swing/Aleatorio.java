package pt51_swing;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Aleatorio {

	public static void main(String[] args) {
		
		new VentanaEx2();
	}

}
class VentanaEx2 extends JFrame{
	private JPanel panelPrincipal,panelSup,panelSup1,panelSup2,panelInf;
	private JTextField tnum1,tnum2,tresult,tintentos,taciertos,tfallas;
	private JLabel enum1,enum2,eresult,eintentos,eaciertos,efallas;
	private JButton bActivar,bComprobar,bSalir;


	
	public VentanaEx2(){
		
		setBounds(200,200,500,200);
		setTitle("ex2 pt51 Aleatori");
		initComponents();
		
		setResizable(false);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	
	public void initComponents() {
		
		panelPrincipal = new JPanel();
		panelPrincipal.setLayout(new BorderLayout()); 
		add(panelPrincipal);
		
//		panelCentral = new JPanel();
//		panelCentral.setLayout(new BoxLayout(panelCentral,BoxLayout.X_AXIS)); // Ajustamos valores para que solo haya una fila y dos columnas (los paneles)
		
		
		panelSup = new JPanel();
		panelSup1 = new JPanel();
		panelSup2 = new JPanel();
		panelSup.setLayout(new GridLayout(2,1));
		
		
		panelInf = new JPanel();
		//panelInf.setLayout(new BoxLayout(panelInf,BoxLayout.X_AXIS));
		panelInf.setLayout(new FlowLayout());
		
//		Superior
		tnum1 = new JTextField(7);
		tnum2 = new JTextField(7);
		tresult = new JTextField(7);
		
		enum1 = new JLabel("Numero 1:");
		enum2 = new JLabel("+ Numero 2:");
		eresult = new JLabel("= Resultado ");
		
		//parte de arriba panelSuperior
		panelSup1.add(enum1);
		panelSup1.add(tnum1);
		panelSup1.add(enum2);
		panelSup1.add(tnum2);
		panelSup1.add(eresult);
		panelSup1.add(tresult);
		panelSup.add(panelSup1);
		
		
		// parte de abajo panelSuperior	
		eintentos = new JLabel("Intentos:");
		eaciertos = new JLabel("Aciertos: ");
		efallas = new JLabel("Fallas: ");
		tintentos = new JTextField(7);
		taciertos = new JTextField(7);
		tfallas = new JTextField(7);
		
		panelSup2.add(eintentos);
		panelSup2.add(tintentos);
		panelSup2.add(eaciertos);
		panelSup2.add(taciertos);
		panelSup2.add(efallas);
		panelSup2.add(tfallas);
		
		panelSup.add(panelSup2);
 // Inferior private JButton bActivar,bComprobar,bSalir;
		
		bActivar = new JButton("Activar");
		bComprobar = new JButton("Comprobar");
		bSalir = new JButton("Salir");
		
		panelInf.add(bActivar);
		panelInf.add(bComprobar);
		panelInf.add(bSalir);
		
		panelPrincipal.add(panelSup);
		panelPrincipal.add(panelInf, BorderLayout.SOUTH);
	}
}