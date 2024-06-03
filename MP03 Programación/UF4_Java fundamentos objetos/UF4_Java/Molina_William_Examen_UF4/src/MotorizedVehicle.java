import java.util.ArrayList;

public abstract class MotorizedVehicle implements Comparable<MotorizedVehicle> {
	private String model;
	private int numWheels;
	private int basePrice;
	private ArrayList <Wheel> wheels = new ArrayList<>();
	private Engine engine;
	
	//constr
	public MotorizedVehicle(String model, int numWheels, int basePrice) {
		super();
		this.model = model;
		this.numWheels = numWheels;
		this.basePrice = basePrice;
		
	}
	
	//setget
	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public int getNumWheels() {
		return numWheels;
	}

	public void setNumWheels(int numWheels) {
		this.numWheels = numWheels;
	}

	public int getBasePrice() {
		return basePrice;
	}

	public void setBasePrice(int basePrice) {
		this.basePrice = basePrice;
	}

	public ArrayList<Wheel> getWheels() {
		return wheels;
	}


	public Engine getEngine() {
		return engine;
	}

	public void setEngine(Engine engine) {
		this.engine = engine;
	}
	
	//metodo abstracto
	
	public abstract int getPrice();
	
	//otros metodos
	
	public void setWheels(ArrayList<Wheel> wheels) {
		int radio = wheels.get(0).getRadio();
		int grosor = wheels.get(0).getThickness();
		
		for (Wheel wheel : wheels) {
			if (wheel.getRadio() != radio) {
				System.out.println("Ruedas son de diferente radio");
			}
			if (wheel.getThickness() != grosor) {
				System.out.println("Ruedas son de diferente grosor");
			}
		}
		
		if (wheels.size() > getNumWheels()) {
			System.out.println("Hay mas o menos ruedas de las permitidas por el vehiculo");
		} else {
			this.wheels = wheels;
		}
	}
	
	
	public void addWheels (Wheel w) {
		if (wheels.size() == 0) {
			wheels.add(w);
			
		}else {
			
			int radio = wheels.get(0).getRadio();
			int grosor = wheels.get(0).getThickness();
			
			if (w.getRadio() != radio) {
				System.out.println("Rueda es de diferente radio");
			}
			if (w.getThickness() != grosor) {
				System.out.println("Rueda es de diferente grosor");
			}
			
		}
	}
	
	//compareTo precio
	
	public int compareTo(MotorizedVehicle mv) {
		return this.getPrice() - mv.getPrice();
	}
	
}
