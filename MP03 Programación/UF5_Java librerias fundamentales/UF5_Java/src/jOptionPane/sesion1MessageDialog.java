package jOptionPane;

import java.awt.BorderLayout;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JTextField;

public class sesion1MessageDialog {

	public static void main(String[] args) {
		new MarcoMessageDialeg();

	}

}

class MarcoMessageDialeg extends JFrame{
	private JPanel panel1;
	private JLabel contrasenya,nom;
	private JTextField jtTexto;
	private JPasswordField password;
	
	public MarcoMessageDialeg() {
		this.setSize(300,180);
		this.setTitle("Cuadros de dialogo");
		initComponents();
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
		this.setResizable(false);
		this.setLocationRelativeTo(null);
	}

	private void initComponents() {
		panel1 = new JPanel();
		panel1.setLayout(new GridLayout(2,2));
		
		password = new JPasswordField(10);
		nom  = new JLabel("NOM: ");
		jtTexto = new JTextField();
		contrasenya = new JLabel("CONTRASENYA: ");
		
		password.addFocusListener(new FocusListener() { //confomrme el cursor lo selecciona o no

		
			public void focusGained(FocusEvent e) {
				//no metemos nada, solo necesitamos hacer algo cuando se peirda el foco
			}

			
			public void focusLost(FocusEvent e) {
				//Comprobación de la  contrasena (si el texto es mas pequeno que 8 OR (||) texto mas grande que 10)
				
				if (password.getPassword().length < 8 || password.getPassword().length>10) {
					JOptionPane.showMessageDialog(null, "La contrasena tiene que tener entre 8 y 10 caracteres!!!",
							"Contrasena incorrecta",JOptionPane.INFORMATION_MESSAGE);
				}
			}	
		});
		
		panel1.add(nom);
		panel1.add(jtTexto);
		panel1.add(contrasenya);
		panel1.add(password);
		
		this.add(panel1,BorderLayout.NORTH);
		
	}
}