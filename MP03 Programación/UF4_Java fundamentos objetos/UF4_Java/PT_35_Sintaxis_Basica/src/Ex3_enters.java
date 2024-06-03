
public class Ex3_enters {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//A
		int operand1;
		int operand2;
		int resultat;
		
		{//B
			System.out.println("DIVISION CON VARIABLES INT");
			
			operand1 = 17;
			operand2 = 3;
			resultat = operand1 / operand2;
			
			System.out.println("Primera división: 17 / 3 = "+resultat);
			
			operand1 = 9;
			operand2 = 3;
			resultat = operand1 / operand2;
			
			System.out.println("Segunda división: 9 / 3 = "+resultat);
			
			operand1 = 21;
			operand2 = 4;
			resultat = operand1 / operand2;
			
			System.out.println("Tercera división: 21 / 4 = "+resultat+"\n");
		}
		
		{ //C
			System.out.println("MODULO CON VARIABLES INT");
			
			operand1 = 17;
			operand2 = 3;
			resultat = operand1 % operand2;
			
			System.out.println("Primer modulo: 17 % 3 = "+resultat);
			
			operand1 = 9;
			operand2 = 3;
			resultat = operand1 % operand2;
			
			System.out.println("Segundo modulo: 9 % 3 = "+resultat);
			
			operand1 = 21;
			operand2 = 4;
			resultat = operand1 % operand2;
			
			System.out.println("Tercer modulo: 21 % 4 = "+resultat+"\n");
			
		}
		{//D
			double operand1d;
			double operand2d;
			double resultatd;
			
			System.out.println("DIVISION CON VARIABLES DOUBLE");
			
			operand1d = 17;
			operand2d = 3;
			resultatd = operand1d / operand2d;
			
			System.out.println("Primera división: 17 / 3 = "+resultatd);
			
			operand1d = 9;
			operand2d = 3;
			resultatd = operand1d / operand2d;
			
			System.out.println("Segunda división: 9 / 3 = "+resultatd);
			
			operand1d = 21;
			operand2d = 4;
			resultatd = operand1d / operand2d;
			
			System.out.println("Tercera división: 21 / 4 = "+resultatd+"\n");
		}

	}

}
