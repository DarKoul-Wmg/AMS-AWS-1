package componentes;

import java.awt.BorderLayout;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;

public class exJTable extends JFrame {
	
	private JTable taula;
	private JScrollPane jsp;
	
	
	public exJTable(){
		
		//nom columnes
		String []nomCol= {"nombre","zona","color"};
		
		//dades taula
		String [][]datos = {{"cobre","kalindor, reinos del este","marron"},{"oro","varias","amarillo"},
				{"cobalto","rasganorte","azul"},{"hierro vil","outlands","verde"},
				{"mitril","kalindor, reinos del este","blanco"}};
		
		taula = new JTable(datos,nomCol);
		taula.setRowHeight(24);
		taula.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);
		
		jsp = new JScrollPane(taula);
		
		
		
		this.add(jsp,BorderLayout.CENTER);
		this.setTitle("JTable... ");
		this.setSize(300, 150);
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}



	public static void main(String[] args) {
	
		new exJTable();
	}

}
