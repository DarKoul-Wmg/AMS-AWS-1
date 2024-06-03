package pt_Extra;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.image.BufferedImage;
import java.util.ArrayList;

import javax.swing.Action;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class JuegoAhorcado {
	public static void main(String[] args) {
		new PreVentanaA();

	}
}

class PreVentanaA extends JFrame{
	private JPanel panelPrincipal,panelCentral,panelLabel,panelTexto,panelBotones, panelError, panelSalir;
	private JLabel etiqueta,etiquetaError;
	private JTextField campoTexto;
	private JButton botonGuardar, botonComenzar, botonSalir;
	
	private String palabraGuardada;
	
	
	
	PreVentanaA() {
		setBounds(100,100,400,400);
		//setTitle(title);
		initComponents();
		
		setLocationRelativeTo(null);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
	}
	

	public void initComponents() {
		panelPrincipal = new JPanel();
		panelPrincipal.setLayout(new BorderLayout());
		
		panelCentral = new JPanel();
		panelCentral.setLayout(new BoxLayout(panelCentral, BoxLayout.Y_AXIS));
		panelBotones = new JPanel();
		
		panelLabel = new JPanel();
		etiqueta = new JLabel("Introduce la palabra a adivinar:");
		panelLabel.add(etiqueta);
		
		panelTexto = new JPanel();
        campoTexto = new JTextField(10); // Ancho del campo de texto
        panelTexto.add(campoTexto);
        
        botonGuardar = new JButton("Guardar");
        botonComenzar = new JButton("Comenzar");
        panelBotones.add(botonGuardar);
        panelBotones.add(botonComenzar);
        
        
        panelError = new JPanel();
        etiquetaError = new JLabel("");
        etiquetaError.setOpaque(true); // Esto ahce que el background de la etiqueta sea visible
        etiquetaError.setBackground(Color.YELLOW);
        panelError.add(etiquetaError);
        
        botonSalir = new JButton("Salir");
        panelSalir = new JPanel();
        panelSalir.add(botonSalir);
        
        panelCentral.add(panelLabel);
        panelCentral.add(panelTexto);
        panelCentral.add(panelBotones);
        panelCentral.add(panelError);
        panelCentral.add(panelSalir);
        
        panelPrincipal.add(panelCentral);
        
        add(panelPrincipal);
        
        //acciones
        
        botonGuardar.addActionListener(new ActionListener() {						
			public void actionPerformed(ActionEvent e) {
				String palabra = campoTexto.getText();
				
				try {
					verificarPalabra(palabra);
					etiquetaError.setText("");
					palabraGuardada = palabra;
					System.out.println(palabraGuardada);
					
				} catch (CaracterNoAlfabeticoException ex) {
					etiquetaError.setText("Excepcion: "+ex.getMessage());
					
				}
			}
		});
        
        botonComenzar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
          
                
                // Verificar si la palabra guardada es válida (no está vacía y es alfabética)
                if (palabraGuardada == null || palabraGuardada.isEmpty()) {
                    etiquetaError.setText("Error: No se ha guardado ninguna palabra válida.");
                } else {
                    // Abre la ventana del juego
                    new MiVentanaAhorcado(palabraGuardada);
                    dispose(); // Cierra la ventana actual
                }
            }
        });
	}

	
	 private void verificarPalabra(String palabra) throws CaracterNoAlfabeticoException {		 
		 for (char ch : palabra.toCharArray()) {
			 if (!Character.isLetter(ch)) {
				 throw new CaracterNoAlfabeticoException("La palabra introducidad no es valida");
	         }
	     }
	 }
	
	
}

class CaracterNoAlfabeticoException extends Exception {
    public CaracterNoAlfabeticoException(String mensaje) {
        super(mensaje);
    }
}



class MiVentanaAhorcado extends JFrame{
	
	private JPanel panelPrincipal, panelCentral, panelPalabra, panelRespuesta, 
				panelTiradas, panelLetras, panelMensaje, panelTerminar,panelEspacio;
	
	private ArrayList<JLabel> letrasOcultas;
	private JTextField areaTexto;
	private JButton botonTirar, botonTerminar;
	private JLabel tiradas, letrasIntroducidas, mensaje;
	
	private String palabraSecreta;
	private String letras = "";
	private int contadorTiradas;
	
	MiVentanaAhorcado(String palabra) {
		palabraSecreta = palabra.toLowerCase();
		
		setBounds(100,100,400,400);	
		initComponents();
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
		setLocationRelativeTo(null);
	}
	
	public void initComponents() {
		panelPrincipal = new JPanel();
		panelPrincipal.setLayout(new BorderLayout());
		
		panelCentral = new JPanel();
		panelCentral.setLayout(new BoxLayout(panelCentral, BoxLayout.Y_AXIS));
		
		panelPalabra = new JPanel();
		panelPalabra.setLayout(new BoxLayout(panelPalabra, BoxLayout.X_AXIS));
		
		//rellenar el panel palabra con un _ por cada letra de la palabra oculta
		letrasOcultas = new ArrayList<JLabel>();
		for (int i = 0; i<palabraSecreta.length(); i++) {
			JLabel letraOculta = new JLabel("_ ");
			panelPalabra.add(letraOculta);
			letrasOcultas.add(letraOculta);
		}
		
		panelCentral.add(panelPalabra);
		panelEspacio = new JPanel();
		panelCentral.add(panelEspacio);
		
		panelRespuesta = new JPanel();
		botonTirar = new JButton("Tirar");
		areaTexto = new JTextField(10);
		
		//panelRespuesta.setLayout(new BoxLayout(panelRespuesta, BoxLayout.X_AXIS));
		panelRespuesta.add(areaTexto);
		panelRespuesta.add(botonTirar);
		panelCentral.add(panelRespuesta);
		
		panelTiradas = new JPanel();
		tiradas = new JLabel("Tiradas "+contadorTiradas+"/10");
		panelTiradas.add(tiradas);
		panelCentral.add(panelTiradas);
		
		panelLetras = new JPanel();
		letrasIntroducidas = new JLabel("Letras Introducidas:"+letras);
		panelLetras.add(letrasIntroducidas);
		panelCentral.add(panelLetras);
		
		panelMensaje = new JPanel();
		mensaje = new JLabel(""); //aqui van todos los mensajes de excepciones y el mensaje confome a adivinado la palabra
		panelMensaje.add(mensaje);
		panelCentral.add(panelMensaje);
		
		panelTerminar = new JPanel();
		botonTerminar = new JButton("Terminar");
		panelTerminar.add(botonTerminar);
		panelTerminar.setVisible(false); //desaparece el panel hasta que acabe la partida
		panelCentral.add(panelTerminar);
        
        panelPrincipal.add(panelCentral);
        
        add(panelPrincipal);
        
        //acciones
        
        botonTerminar.addActionListener(new ActionListener() {
            
        	// Cerrar esta ventana y volver a la ventana anterior
            public void actionPerformed(ActionEvent e) {
                
            	new PreVentanaA();
                dispose(); 
               
            }
        });
        
        botonTirar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String entrada = areaTexto.getText(); //obtener texto
                areaTexto.setText("");  // limpiar area texto
                
                if (entrada.isEmpty()) {
                	entrada = "0";
                }
                
                try {
                    validar(entrada);
                    char letra = entrada.charAt(0);  // primera letra de la entrada

                    if (palabraSecreta.indexOf(letra) != -1) {
                        // La letra esta en la palabra oculta
                        letras += " " + letra;
                        letrasIntroducidas.setText("Letras Introducidas:" + letras);

                        // Actualizamos las JLabels correspondientes con la letra correcta
                        for (int i = 0; i < palabraSecreta.length(); i++) {
                            if (palabraSecreta.charAt(i) == letra) {
                                letrasOcultas.get(i).setText(Character.toString(letra)); //Cambiamos _ por letra
                            }
                        }
                        
                        //comporobacion cada vez que se acierta una letra para saber si esta la palabra completa o no
                        
                        if (palabraResuelta()) {
                            mensaje.setText("Bravo, has adivinado la palabra!!!");
                            panelRespuesta.setVisible(false);
                            panelTerminar.setVisible(true);
                        }
                        
                                    
                    } else {
                    	//No esta en la palabra oculta
                    	letras += " " + letra;
                    	letrasIntroducidas.setText("Letras Introducidas:" + letras);
                        contadorTiradas++;
                        tiradas.setText("Tiradas " + contadorTiradas + "/10");
                        
                        if (contadorTiradas >= 10) {
                            mensaje.setText("Has superado el límite de tiradas");
                            panelRespuesta.setVisible(false);
                            panelTerminar.setVisible(true);
                        }
                    }
                        
                                        

                } catch (CaracterNoAlfabeticoException ex) {
                    mensaje.setText(ex.getMessage());
                    panelMensaje.repaint();  // Actualizamos el panel para mostrar el mensaje de excepción
                }
            }

            // Validamos que la entrada esté compuesta solo de letras
            private void validar(String entrada) throws CaracterNoAlfabeticoException {
                for (char c : entrada.toCharArray()) {
                    if (!Character.isLetter(c)) {
                        throw new CaracterNoAlfabeticoException("Exception: Has de introducir una letra válida");
                    }
                }
            }
        });

	}
	private boolean palabraResuelta() {
        for (JLabel letraLabel : letrasOcultas) {
            if (letraLabel.getText().equals("_ ")) {
                return false; // Hay al menos una letra no revelada
            }
        }
        return true; // Todas las letras han sido reveladas
    }

}