import java.util.ArrayList;

public class Portatil extends Dispositivo implements Recargable  {
	private Bateria bateria;
	
	//constr
	public Portatil(Cpu cpu, Ram ram, Bateria bateria, ArrayList<Hdd> discos,int precioBase) {
		super(cpu, ram, precioBase, discos);
		this.bateria = bateria;
	}
	
	//setGet
	public Bateria getBateria() {
		return bateria;
	}
	
	
	public void recargarBateria() {
		bateria.setNivelBateria(100);
		
	}
	
	//metodo abs de clase padre
	public int getPrecioTotal(){
		int precioTotal = getPrecioBase();
		
		precioTotal+= getCpu().getPrecio();
		precioTotal+= getRam().getPrecio();
		
		for (Hdd disco : getDiscos()) {
			precioTotal += disco.getPrecio();
		}
		
		precioTotal+= bateria.getPrecio();
		
		return precioTotal;
	}
	
	public String toString() {
		String listaDiscos = "\n-Discos\n";
		for(Hdd disco : getDiscos()) {
			listaDiscos += disco.toString(); 
		}
		return "Portatil\n"+getCpu().toString()+getRam().toString()+ listaDiscos + bateria.toString()+"Precio "+getPrecioTotal();
	}

}
