
public abstract class Engine {
	
	private String model;
	private int power;
	private int basePrice;
	private int maxSpeed;
	
	//constr
	public Engine(String model, int power, int basePrice, int maxSpeed) {
		super();
		this.model = model;
		this.power = power;
		this.basePrice = basePrice;
		this.maxSpeed = maxSpeed;
	}
	
	//getset
	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public int getPower() {
		return power;
	}

	public void setPower(int power) {
		this.power = power;
	}

	public int getBasePrice() {
		return basePrice;
	}

	public void setBasePrice(int basePrice) {
		this.basePrice = basePrice;
	}

	public int getMaxSpeed() {
		return maxSpeed;
	}

	public void setMaxSpeed(int maxSpeed) {
		this.maxSpeed = maxSpeed;
	}
	
	
}
