import java.util.ArrayList;

public class PCMesa extends Dispositivo {

	public PCMesa(Cpu cpu, Ram ram, ArrayList<Hdd> discos, int precioBase) {
		super(cpu, ram, precioBase, discos);
	
	}
	
	//metodo abs de clase padre
		
	public int getPrecioTotal(){
		int precioTotal = getPrecioBase();
		
		precioTotal+= getCpu().getPrecio();
		precioTotal+= getRam().getPrecio();
		
		for (Hdd disco : getDiscos()) {
			precioTotal += disco.getPrecio();
		}
			
		return precioTotal;
	}


	public String toString() {
		String listaDiscos = "\n-Discos\n";
		for(Hdd disco : getDiscos()) {
			listaDiscos += disco.toString(); 
		}
		return "PCMesa\n"+getCpu().toString()+getRam().toString()+ listaDiscos +"Precio "+getPrecioTotal();
	}

}
