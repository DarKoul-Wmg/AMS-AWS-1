package pt_Extra;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.util.Random;

import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;





public class juegoMente {
	public static void main(String[] args) {
		new PreVentanaM();

	}
}

class PreVentanaM extends JFrame {
    private JPanel panelPrincipal, panelCentral, panelEtiqueta, panelError, panelNombre, panelBotones;
    private JLabel etiqueta1, etiquetaError, etiquetaNombre;
    private JTextField campoTexto;
    private JButton botonStart, botonFinish;

    PreVentanaM() {
        setBounds(100, 100, 400, 400);
        //setTitle(title);
        initComponents();

        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    public void initComponents() {
        // Crear paneles
        panelPrincipal = new JPanel();
        panelPrincipal.setLayout(new BorderLayout());
        panelCentral = new JPanel();
        panelCentral.setLayout(new BoxLayout(panelCentral, BoxLayout.Y_AXIS));

        panelEtiqueta = new JPanel();
        panelError = new JPanel();
        panelNombre = new JPanel();
        panelBotones = new JPanel();

        // Crear etiquetas
        etiqueta1 = new JLabel("MINI MASTERMIND");
        etiqueta1.setFont(new Font("Arial", Font.BOLD, 20));
        etiquetaError = new JLabel("");
        etiquetaNombre = new JLabel("NOM");

        // Crear campo de texto
        campoTexto = new JTextField(15);

        // Crear botones
        botonStart = new JButton("Start");
        botonFinish = new JButton("Finish");

        // Agregar componentes a los paneles
        panelEtiqueta.add(etiqueta1);
        panelError.add(etiquetaError);
        panelNombre.add(etiquetaNombre);
        panelNombre.add(campoTexto);

        panelBotones.add(botonStart);
        panelBotones.add(botonFinish);

        // Agregar paneles al panel central
        panelCentral.add(panelEtiqueta);
        panelCentral.add(panelError);
        panelCentral.add(panelNombre);
        panelCentral.add(new JPanel()); // Panel vacío para espaciar
        panelPrincipal.add(panelBotones,BorderLayout.SOUTH);

        // Agregar panel central al panel principal
        panelPrincipal.add(panelCentral, BorderLayout.CENTER);

        // Agregar panel principal al frame
        add(panelPrincipal);

        // Acción para el botón "Start"
        botonStart.addActionListener(new ActionListener() {
      
            public void actionPerformed(ActionEvent e) {
                String nombre = campoTexto.getText();
                try {
                    validarNombre(nombre);                   
                    new VentanaJuego(nombre);
                    dispose();
                   
                } catch (NombreInvalidoException ex) {
                    etiquetaError.setText(ex.getMessage());
                }
            }
        });

        // Acción para el botón "Finish"
        botonFinish.addActionListener(new ActionListener() {
          
            public void actionPerformed(ActionEvent e) {
            	System.exit(0);
                dispose(); // Cerrar la ventana principal
            }
        });
    }

    private void validarNombre(String nombre) throws NombreInvalidoException {
        // Validar que el nombre contenga letras y números
        boolean contieneLetras = false;
        boolean contieneNumeros = false;

        for (char c : nombre.toCharArray()) {
            if (Character.isLetter(c)) {
                contieneLetras = true;
            } else if (Character.isDigit(c)) {
                contieneNumeros = true;
            }
        }
        
     // Si falta letra numero
        if (!contieneLetras || !contieneNumeros) {
            throw new NombreInvalidoException("Nom incorrecte");
        }

        
    }
}
class NombreInvalidoException extends Exception {
    public NombreInvalidoException(String mensaje) {
        super(mensaje);
    }
}

class VentanaJuego extends JFrame {
    private JPanel panelPrincipal, panelCentral, panelNombreJugador, panelLabels,
            panelNumeros, panelMensajes, panelBotones;

    private JLabel etiquetaNombre, etiquetaIntentos;
    private JLabel[] labelsColores, labelsResultado;
    private JTextField[] camposNumeros;

    private JTextField campoMensajes;

    private JButton botonCheck, botonBack, botonRemove;

    private int contadorIntentos;
    private int[] combinacionAleatoria;

    VentanaJuego(String nombreJugador) {
        setBounds(100, 100, 400, 400);
        setTitle("Juego de Adivinanza");
        initComponents(nombreJugador);

        setLocationRelativeTo(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    public void initComponents(String nombreJugador) {
        contadorIntentos = 0;

        // Generar combinación aleatoria de 4 colores
        combinacionAleatoria = generarCombinacionAleatoria();

        // Inicializar paneles
        panelPrincipal = new JPanel(new BorderLayout());
        panelCentral = new JPanel();
        panelCentral.setLayout(new BoxLayout(panelCentral, BoxLayout.Y_AXIS));
        
        panelNombreJugador = new JPanel();      
        panelLabels = new JPanel();   
        panelNumeros = new JPanel();
        panelMensajes = new JPanel();
        panelBotones = new JPanel();

        // Inicializar etiquetas
        etiquetaNombre = new JLabel("Jugador: " + nombreJugador);
        etiquetaIntentos = new JLabel("INTENTO: " + contadorIntentos + "/5");

        // Inicializar arrays de JLabel y JTextField
        labelsColores = new JLabel[4];
        labelsResultado = new JLabel[4];
        camposNumeros = new JTextField[4];
        for (int i = 0; i < 4; i++) {
            labelsColores[i] = new JLabel();
            labelsResultado[i] = new JLabel();
            camposNumeros[i] = new JTextField(5);
            panelLabels.add(labelsColores[i]);
            panelLabels.add(labelsResultado[i]);
            panelNumeros.add(camposNumeros[i]);
        }

        // Inicializar campo de mensajes y botones
        campoMensajes = new JTextField(20);
        campoMensajes.setEditable(false); // No editable

        botonCheck = new JButton("Check");
        botonBack = new JButton("Back");
        botonRemove = new JButton("Remove");

        // Acciones para los botones
        botonCheck.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    comprobarCombinacion();
                } catch (ValueException ex) {
                    campoMensajes.setText("Valor no válido: " + ex.getMessage());
                }
            }
        });

        botonBack.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Volver a la ventana inicial
                // Aquí debes llamar al método que muestra la ventana inicial
                // por ejemplo: mostrarVentanaInicial();
                dispose(); // Cerrar ventana de juego
            }
        });

        botonRemove.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Limpiar los JTextField de números
                for (JTextField campo : camposNumeros) {
                    campo.setText("");
                }
                // Limpiar mensajes
                campoMensajes.setText("");
            }
        });

        // Agregar botones al panel de botones
        panelBotones.add(botonCheck);
        panelBotones.add(botonRemove);
        panelBotones.add(botonBack);

        // Agregar componentes a los paneles y al panel principal
        panelNombreJugador.add(etiquetaNombre);
        
        panelCentral.add(panelNombreJugador);
        panelCentral.add(panelLabels);
        panelCentral.add(panelNumeros);
        panelCentral.add(panelBotones);
        panelCentral.add(etiquetaIntentos);
        panelMensajes.add(campoMensajes);

        panelPrincipal.add(panelCentral, BorderLayout.CENTER);
        panelPrincipal.add(panelMensajes, BorderLayout.SOUTH);

        add(panelPrincipal);
    }

    private int[] generarCombinacionAleatoria() {
        Random random = new Random();
        int[] combinacion = new int[4];
        for (int i = 0; i < 4; i++) {
            combinacion[i] = random.nextInt(6) + 1; // Números aleatorios del 1 al 6
        }
        return combinacion;
    }

    private void comprobarCombinacion() throws ValueException {
        int[] intento = new int[4];
        try {
            for (int i = 0; i < 4; i++) {
                intento[i] = Integer.parseInt(camposNumeros[i].getText());
                if (intento[i] < 1 || intento[i] > 6) {
                    throw new ValueException("Valor no válido. Debe estar entre 1 y 6.");
                }
            }
        } catch (NumberFormatException ex) {
            throw new ValueException("Valor no válido. Debe ser un número.");
        }

        // Contar MORTS y FERITS
        int morts = 0, ferits = 0;
        boolean[] marcadoCombinacion = new boolean[4];
        boolean[] marcadoIntento = new boolean[4];

        // Contar MORTS (colores correctos en la posición correcta)
        for (int i = 0; i < 4; i++) {
            if (combinacionAleatoria[i] == intento[i]) {
                morts++;
                marcadoCombinacion[i] = true;
                marcadoIntento[i] = true;
            }
        }

        // Contar FERITS (colores correctos en la posición incorrecta)
        for (int i = 0; i < 4; i++) {
            if (!marcadoIntento[i]) {
                for (int j = 0; j < 4; j++) {
                    if (!marcadoCombinacion[j] && intento[i] == combinacionAleatoria[j]) {
                        ferits++;
                        marcadoCombinacion[j] = true;
                        break;
                    }
                }
            }
        }

        contadorIntentos++;
        etiquetaIntentos.setText("INTENTO: " + contadorIntentos + "/5");

        if (morts == 4) {
            campoMensajes.setText("¡HAS GANADO!");
            // Aquí debes mostrar la combinación oculta
        } else if (contadorIntentos >= 5) {
            campoMensajes.setText("You lost: GAME OVER");
            // Aquí debes mostrar la combinación oculta
        } else {
            campoMensajes.setText("Morts: " + morts + ", Ferits: " + ferits);
        }
    }

    class ValueException extends Exception {
        public ValueException(String mensaje) {
            super(mensaje);
        }
    }
}
	

