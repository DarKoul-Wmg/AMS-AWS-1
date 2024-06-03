import java.util.ArrayList;

public abstract class Dispositivo implements Comparable<Dispositivo> {
	private Cpu cpu;
	private Ram ram;
	private int precioBase;
	private ArrayList <Hdd> discos = new ArrayList<>();
	
	//Constructor
	
	public Dispositivo(Cpu cpu, Ram ram, int precioBase, ArrayList<Hdd> discos) {
		super();
		this.cpu = cpu;
		this.ram = ram;
		this.precioBase = precioBase;
		this.discos = discos;
	}
	
	//GetSet
	public Cpu getCpu() {
		return cpu;
	}
	
	public void setCpu(Cpu cpu) {
		this.cpu = cpu;
	}
	public Ram getRam() {
		return ram;
	}
	public void setRam(Ram ram) {
		this.ram = ram;
	}
	public int getPrecioBase() {
		return precioBase;
	}
	public void setPrecioBase(int precioBase) {
		this.precioBase = precioBase;
	}
	public ArrayList<Hdd> getDiscos() {
		return discos;
	}
	public void setDiscos(ArrayList<Hdd> discos) {
		this.discos = discos;
	}
	
	//metodos
	
	public void addDisk(Hdd disco){
		discos.add(disco);
	}
	
	public int getDiskCapacity() {
		int capacidadTotal = 0;
		
		for (Hdd disco : discos) {
			capacidadTotal += disco.getCapacidad(); 
		}
		
			return capacidadTotal;
	}
	
	public abstract int getPrecioTotal();
	
	//compare Precio
	
	public int compareTo(Dispositivo d) {
		return this.getPrecioTotal() - d.getPrecioTotal();
	}
	
}
