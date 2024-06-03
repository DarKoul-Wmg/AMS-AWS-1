
public class CombustionEngine extends Engine {
	
	private float comsumption;
	private int engineDisplacement;
	
	// constr
	public CombustionEngine(String model, int power, int basePrice, int maxSpeed, int engineDisplacement, float comsumption) {
		super(model, power, basePrice, maxSpeed);
		this.engineDisplacement = engineDisplacement;
		this.comsumption = comsumption;
		
	}
	
	//setget
	public float getComsumption() {
		return comsumption;
	}

	public void setComsumption(float comsumption) {
		this.comsumption = comsumption;
	}

	public int getEngineDisplacement() {
		return engineDisplacement;
	}

	public void setEngineDisplacement(int engineDisplacement) {
		this.engineDisplacement = engineDisplacement;
	}
	
	//toString
		public String toString() {
			return "Combustion Engine\n****************\n"
					+ "Model = "+getModel()+"\nPower = "+getPower()+"\nEngine Displacement = "+getEngineDisplacement()+"\nMaxSpeed = "+getMaxSpeed()
					+"\nComsumption = " + comsumption + "\nPrice = " + getBasePrice()+"\n";
		}
	

}
