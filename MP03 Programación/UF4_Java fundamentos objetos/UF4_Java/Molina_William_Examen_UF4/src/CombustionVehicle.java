
public class CombustionVehicle extends MotorizedVehicle implements FillTank{
	
	private int tankCapacity;
	private int tankLevel = 0;
	
	//constr
	public CombustionVehicle(String model, int numWheels, int basePrice, CombustionEngine engine, int tankCapacity) {
		super(model, numWheels, basePrice);
		
		setEngine(engine);
		this.tankCapacity = tankCapacity;
	}
	
	
	//setget

	public int getTankCapacity() {
		return tankCapacity;
	}


	public void setTankCapacity(int tankCapacity) {
		this.tankCapacity = tankCapacity;
	}


	public int getTankLevel() {
		return tankLevel;
	}


	public void setTankLevel(int tankLevel) {
		this.tankLevel = tankLevel;
	}
	
	
	//metodo abstracto clase padre
	public int getPrice() {
		int precioTotal = getBasePrice();
		precioTotal = getEngine().getBasePrice();
		
		for (Wheel wheel : getWheels()) {
			precioTotal += wheel.getBasePrice();
		}
		
		return precioTotal;
	
	}
	
	//metodo interfaz
	public void fill() {
			setTankLevel(100);
			
		}

	//to String
	public String toString() {
		String listaRuedas = "\n-Wheels\n";
		for(Wheel wheel : getWheels()) {
			listaRuedas += wheel.toString(); 
		}
		return "\n########################\n"
				+ "Combustion Vehicle"
				+ "\n########################\n"
				+ "\nModel = "+getModel().toString()+"\nBase Price = "+getBasePrice()+"\n"
				+ getEngine().toString()+ listaRuedas+"\nTotal Price = "+getPrice()+"\n";
	}

}
