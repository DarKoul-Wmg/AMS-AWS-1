
public class Wheel {
	
	private String model;
	private int basePrice;
	private int radio;
	private int thickness;
	
	//constr
	public Wheel(String model, int basePrice, int radio, int thickness) {
		super();
		this.model = model;
		this.basePrice = basePrice;
		this.radio = radio;
		this.thickness = thickness;
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

	public int getRadio() {
		return radio;
	}

	public void setRadio(int radio) {
		this.radio = radio;
	}

	public int getThickness() {
		return thickness;
	}

	public void setThickness(int thickness) {
		this.thickness = thickness;
	}

	//toString
	public String toString() {
		return "\nWheel\n****************\n"
				+ "Model = "+getModel()+"\nRadio = "+getRadio() + "; Thickness = "+getThickness()
				+ "; Price = "+getBasePrice()+"\n";
	}
	
	
	
	
}
