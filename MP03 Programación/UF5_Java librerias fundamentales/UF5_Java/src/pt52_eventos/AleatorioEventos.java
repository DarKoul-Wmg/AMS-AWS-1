package pt52_eventos;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Random;

import javax.imageio.ImageIO;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class AleatorioEventos {

	public static void main(String[] args) {
		
		new VentanaEx2();
	}

}
class VentanaEx2 extends JFrame{
	private JPanel panelPrincipal,panelSup,panelSup1,panelSup2,panelInf;
	private JTextField tnum1,tnum2,tresult,tintentos,taciertos,tfallas;
	private JLabel enum1,enum2,eresult,eintentos,eaciertos,efallas;
	private JButton bActivar,bComprobar,bSalir;
	private int num1,num2,resultadoCorrecto,intentos,aciertos,fallos;
	private Random random = new Random();


	
	public VentanaEx2(){
		
		setBounds(200,200,500,200);
		setTitle("ex2 pt52 Aleatori_events");
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
		
//	Superior
		
		//valores random apra la suma
		num1  = random.nextInt(501);
		num2  = random.nextInt(501);
		resultadoCorrecto = num1 + num2;
		
		tnum1 = new JTextField(String.valueOf(num1),7);
		tnum1.setEditable(false);
		tnum2 = new JTextField(String.valueOf(num2),7);
		tnum2.setEditable(false);
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
		
		tintentos = new JTextField("0",7);
		tintentos.setEditable(false);
		
		taciertos = new JTextField("0",7);
		taciertos.setEditable(false);
		
		tfallas = new JTextField("0",7);
		tfallas.setEditable(false);
		
		panelSup2.add(eintentos);
		panelSup2.add(tintentos);
		panelSup2.add(eaciertos);
		panelSup2.add(taciertos);
		panelSup2.add(efallas);
		panelSup2.add(tfallas);
		
		panelSup.add(panelSup2);
 // Inferior private JButton bActivar,bComprobar,bSalir;
		
		bActivar = new JButton("Activar");
		bActivar.addActionListener(new EventosBotones());
		
		bComprobar = new JButton("Comprobar");
		bComprobar.addActionListener(new EventosBotones());
		
		bSalir = new JButton("Salir");
		bSalir.addActionListener(new EventosBotones());
		
		panelInf.add(bActivar);
		panelInf.add(bComprobar);
		panelInf.add(bSalir);
		
		panelPrincipal.add(panelSup);
		panelPrincipal.add(panelInf, BorderLayout.SOUTH);
	}
	
	class EventosBotones implements ActionListener{

		public void actionPerformed(ActionEvent e) {
			if(e.getSource() == bSalir) {
				System.out.println("Saliendo de la aplicacion...");
				System.exit(0);
			}
			
			if(e.getSource() == bActivar) {
				//Se actualizan los campos
				num1  = random.nextInt(501);
				num2  = random.nextInt(501);
				
				tnum1.setText(String.valueOf(num1));
				tnum2.setText(String.valueOf(num2));
				resultadoCorrecto = num1 + num2;
			}
			
			if(e.getSource() == bComprobar) {
				int result,intent;
				
				try {
					//sacamos el valor introducido por el usuario y lo pasamos a Int
					result = Integer.parseInt(tresult.getText());
					
					//Comprobacion conforme el resultao coincide, suma aciertos
					if (result == resultadoCorrecto) {
						int aciertos;
						System.out.println("Resultado Correcto!!!");
						aciertos = Integer.parseInt(taciertos.getText());
						taciertos.setText(String.valueOf(aciertos + 1));
						
						//reiniciamos valores
						num1  = random.nextInt(501);
						num2  = random.nextInt(501);
						
						tnum1.setText(String.valueOf(num1));
						tnum2.setText(String.valueOf(num2));
						resultadoCorrecto = num1 + num2;
						
					}else { //Si no es correcto, suma fallo
						int fallos;
						System.out.println("Resultado Incorrecto!!!");
						fallos = Integer.parseInt(tfallas.getText());
						tfallas.setText(String.valueOf(fallos + 1));
					}
				}catch(NumberFormatException ex){
					System.out.println("Error, el valor debe ser numerico y entero");
					
				}
				
				intent = Integer.parseInt(tintentos.getText());
				tintentos.setText(String.valueOf(intent +1));
				
				
			}
		}
		
	}
	
	//Controlamos el error de valores no numericos en la string resultado
	public class ValorNoNumericoException extends RuntimeException {
	    public ValorNoNumericoException(String mensaje) {
	        super(mensaje);
	    }
	}

}