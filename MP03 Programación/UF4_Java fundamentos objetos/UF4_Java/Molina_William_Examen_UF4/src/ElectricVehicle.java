import java.util.ArrayList;

public class ElectricVehicle extends MotorizedVehicle implements ChargeBattery{
	
	private int numMaxBatterys;
	private int batteryLevel = 0;
	private ArrayList <Battery> batteries = new ArrayList<>();
	
	//constr
	public ElectricVehicle(String model, int numWheels, int basePrice, ElectricEngine engine, int numMaxBatterys ) {
		super(model, numWheels, basePrice);
		
		setEngine(engine);
		this.numMaxBatterys = numMaxBatterys;
	}
	
	//getset
	public int getNumMaxBatterys() {
		return numMaxBatterys;
	}

	public void setNumMaxBatterys(int numMaxBatterys) {
		this.numMaxBatterys = numMaxBatterys;
	}

	public int getBatteryLevel() {
		return batteryLevel;
	}

	public void setBatteryLevel(int batteryLevel) {
		this.batteryLevel = batteryLevel;
	}

	public ArrayList<Battery> getBatteries() {
		return batteries;
	}

	
	//metodo asbr clase padre
	public int getPrice() {
		int precioTotal = getBasePrice();
		precioTotal = getEngine().getBasePrice();
		
		for (Wheel wheel : getWheels()) {
			precioTotal += wheel.getBasePrice();
		}
		
		for (Battery battery : getBatteries()){
			precioTotal += battery.getBasePrice();
		}
		
		return precioTotal;
	
	}
	
	//metodo interfaz
	public void charge() {
		setBatteryLevel(100);
		
	}
	
	//otros metodos
	
	public void setBatteries(ArrayList<Battery> batteries) {

		
		if (batteries.size() > getNumMaxBatterys()) {
			System.out.println("Hay mas baterias de las permitidas por el vehiculo");
		}else {
			this.batteries = batteries;
		}
	}
	
	
	public void addBattery (Battery b) {
		
		if (batteries.size() >= getNumMaxBatterys()) {
			System.out.println("No se puede añadir la bateria, numero maximo alcanzado");
			
		}else {
			batteries.add(b);
		}
	}
	
	public float getBateryLevel() {
		int total = 0;
		
		for(Battery battery : getBatteries()) {
			total += battery.getBatteryLevel(); 
		}
		float media = total/batteries.size();
		
		return media;
	}
	
	//toString
	public String toString() {
		String listaRuedas = "\n-Wheels\n";
		for(Wheel wheel : getWheels()) {
			listaRuedas += wheel.toString(); 
		}
		String listaBaterias = "\n-Bateries\n";
		for(Battery battery : getBatteries()) {
			listaBaterias += battery.toString(); 
		}
		return "\n########################\n"
				+ "Electric Vehicle"
				+ "\n########################\n"
				+ "\nModel = "+getModel().toString()+"\nBase Price = "+getBasePrice()+"\n"
				+ getEngine().toString()+ listaRuedas+listaBaterias+"\nTotal Price = "+getPrice()+"\n";
	}
}
