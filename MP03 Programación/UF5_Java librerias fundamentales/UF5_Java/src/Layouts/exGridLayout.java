package Layouts;

import java.awt.BorderLayout;
import java.awt.GridBagLayout;
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class exGridLayout extends JFrame {
	
	public exGridLayout() {
		//instanciamos el panel
		
		Marco panel = new Marco();
		this.add(panel,BorderLayout.CENTER);
		this.setTitle("Grid Layout");
		//(this.pack();
		this.setSize(300,300);
		this.setResizable(false);
		this.setVisible(true);
		
		
	}

	public static void main(String[] args) {
		new exGridLayout();
	}

}

class Marco extends JPanel{
	JButton boton[] = new JButton[16];
	
	public Marco(){					//filas,columnas,separaciones
		this.setLayout(new GridLayout(4,4,10,10));
		for(int i = 0; i<10;i++) {
			boton[i] = new JButton(String.valueOf(i)); //convierte entero en string
		}
		boton[10] = new JButton("+");
		boton[11] = new JButton("-");
		boton[12] = new JButton("/");
		boton[13] = new JButton("%");
		boton[14] = new JButton("C");
		boton[15] = new JButton("=");
		
		//Order de botones segun calculadora
		
		for(int i = 7; i<10 ;i++) {
			this.add(boton[i]);
		}
		
		this.add(boton[14]);
		
		for(int i = 4; i<7 ;i++) {
			this.add(boton[i]);
		}
		
		this.add(boton[13]);
		
		for(int i = 1; i<4 ;i++) {
			this.add(boton[i]);
		}
		
		this.add(boton[12]);
		this.add(boton[11]);
		this.add(boton[10]);
		this.add(boton[15]);
	}
	
}