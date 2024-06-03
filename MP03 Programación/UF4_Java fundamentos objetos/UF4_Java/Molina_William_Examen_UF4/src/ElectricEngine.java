
public class ElectricEngine extends Engine {
	
	private int comsumption;
	
	//constr
	public ElectricEngine(String model, int power, int basePrice, int maxSpeed, int comsumption) {
		super(model, power, basePrice, maxSpeed);
		this.comsumption = comsumption;
	}
	
	//setget
	public int getComsumption() {
		return comsumption;
	}

	public void setComsumption(int comsumption) {
		this.comsumption = comsumption;
	}


	//toString
	public String toString() {
		return "Electric Engine\n****************\n"
				+ "Model = "+getModel()+"\nPower = "+getPower()+"\nMaxSpeed = "+getMaxSpeed()
				+"\nComsumption = " + comsumption + "\nPrice = " + getBasePrice()+"\n";
	}

	
	
	

}
