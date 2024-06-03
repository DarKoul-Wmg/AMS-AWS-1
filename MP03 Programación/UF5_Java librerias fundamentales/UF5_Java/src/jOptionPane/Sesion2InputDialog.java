package jOptionPane;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

public class Sesion2InputDialog {

	public static void main(String[] args) {
		
		new MarcoInputDialog();

	}
}	
class MarcoInputDialog extends JFrame{
	private ButtonGroup grupo;
	private JRadioButton estudia,trabaja;
	private JLabel nom,estudiosRealizados;
	private JTextField jtNom;
	private JPanel panel,panelBoton;

	
	public MarcoInputDialog() {
		this.setSize(300,200);
		this.setTitle("Quadre showInputDialog");
		initComponents();
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setVisible(true);
		this.setResizable(false);
		this.setLocationRelativeTo(null);
	}


	private void initComponents() {
		panel = new JPanel(new GridLayout(2,2));
		nom = new JLabel("NOM:");
		
		nom.setHorizontalAlignment(SwingConstants.RIGHT);
		estudiosRealizados = new JLabel("");
		estudia = new JRadioButton("ESTUDIA");
		trabaja = new JRadioButton("TRABAJA");
		estudia.addActionListener(new ActionListener() {
			
			public void actionPerformed(ActionEvent e) {
				if (estudia.isSelected()) {
					String [] opcions = {"AWS1","AM1","AMWS1"};
					String respuesta = (String) JOptionPane.showInputDialog(null, "Seleccione una opcion: ",
											"Estudios en curso",JOptionPane.OK_CANCEL_OPTION,null,opcions,null);
					estudiosRealizados.setText(respuesta);
				}
				
			}
		});
		
		trabaja.addChangeListener(new ChangeListener() {
			
		
			public void stateChanged(ChangeEvent e) {
				if (trabaja.isSelected()) {
					estudiosRealizados.setText("");
				}
				
			}
		});
		
		jtNom = new JTextField(20);
		grupo = new ButtonGroup();
		grupo.add(estudia);
		grupo.add(trabaja);
		panelBoton = new JPanel();
		panelBoton.setLayout(new BoxLayout(panelBoton, BoxLayout.Y_AXIS));
		panelBoton.add(estudia);
		
		panelBoton.add(trabaja);
		panel.add(nom);
		panel.add(jtNom);
		panel.add(estudiosRealizados);
		panel.add(panelBoton);
		
		this.add(panel,BorderLayout.NORTH);
		
	}

}
