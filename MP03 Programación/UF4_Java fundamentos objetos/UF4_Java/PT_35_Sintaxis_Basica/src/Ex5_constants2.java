
public class Ex5_constants2 {
	
	public static final double CONVERSIO_EURO_A_DOLAR = 1.3656;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//B
		double valor = 12.0;
		System.out.println(valor*CONVERSIO_EURO_A_DOLAR);
		valor = 300.0;
		System.out.println(valor*CONVERSIO_EURO_A_DOLAR); //error ortografico (CONVRESIO_EURO_A_DOLAR)
		valor = 189.0;
		System.out.println(valor*CONVERSIO_EURO_A_DOLAR);

	}

}

/*	
16.3872
409.67999999999995
258.09839999999997
*/