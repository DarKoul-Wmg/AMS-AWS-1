package componentes;

import java.awt.BorderLayout;

import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTree;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.DefaultTreeModel;

public class exJTree extends JFrame {
	private JScrollPane jsp;
	private JTree arbol;
	
	public exJTree(){
		
		//Nom columnes
		DefaultMutableTreeNode asig = new DefaultMutableTreeNode("JAVA");
		DefaultTreeModel java = new DefaultTreeModel(asig);
		DefaultMutableTreeNode tema = null;
		DefaultMutableTreeNode seccio = null;
		
		tema = new DefaultMutableTreeNode("Entrada/Sortida. senalitzacio");
		asig.add(tema);
		seccio = new DefaultMutableTreeNode("Entrada baix nivell");
		tema.add(seccio);
		seccio = new DefaultMutableTreeNode("Entrada filtrada Bytes");
		tema.add(seccio);
		seccio = new DefaultMutableTreeNode("Sortida filtrada Bytes");
		tema.add(seccio);
		
		tema = new DefaultMutableTreeNode("Interface Grafica");
		asig.add(tema);
		seccio = new DefaultMutableTreeNode("Layouts");
		tema.add(seccio);
		seccio = new DefaultMutableTreeNode("Events");
		tema.add(seccio);
		
		arbol = new JTree(java);
		jsp = new JScrollPane(arbol);
		
		
		
		this.add(jsp,BorderLayout.CENTER);
		this.setTitle("JTree... ");
		this.setSize(300, 150);
		this.setVisible(true);
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
	}
	
	public static void main(String[] args) {
		
		new exJTree();
	}
}
