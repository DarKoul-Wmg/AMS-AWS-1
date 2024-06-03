
public class Battery {
	
	private String model;
	private int basePrice;
	private int capacity;
	private int power;
	private int batteryLevel = 0;
	
	//Construct
	public Battery(String model, int basePrice, int capacity, int power) {
		super();
		this.model = model;
		this.basePrice = basePrice;
		this.capacity = capacity;
		this.power = power;
	}
	
	//setget
	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public int getBasePrice() {
		return basePrice;
	}

	public void setBasePrice(int basePrice) {
		this.basePrice = basePrice;
	}

	public int getCapacity() {
		return capacity;
	}

	public void setCapacity(int capacity) {
		this.capacity = capacity;
	}

	public int getPower() {
		return power;
	}

	public void setPower(int power) {
		this.power = power;
	}

	public int getBatteryLevel() {
		return batteryLevel;
	}

	public void setBatteryLevel(int batteryLevel) {
		this.batteryLevel = batteryLevel;
	}
	
	//toString
		public String toString() {
			return "\nBattery\n****************\n"
					+ "Model = "+getModel()+"\nPower = "+getPower() + "; Capacity = "+getCapacity()
					+ "; Battery Level = "+getBatteryLevel()+"; Price = "+getBasePrice() +"\n";
		}
	
	
	
}
