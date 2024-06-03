
public class Ex4_operadors {
		public static void main(String[] args) {
			
			//A
			{
				System.out.println("EXA");
				int a=9;
				int b=9;
				System.out.println(a++); //Primero hace la acción de printear a y luego realiza la suma
				System.out.println(++b);// Primero realiza la suma y luego printea b
			}
			
			//B
			{
				System.out.println("\nEXB");
				System.out.println(4 == 4); //booleano true confome se cumple la condición
				System.out.println(5 > 6); //booleano false conforme la condición no se cumple
				System.out.println(7 < 10); //booleano true confome se cumple la condición
			}
			
			{
				System.out.println("\nEXC");
				System.out.println(8.5 + 3.2);
				System.out.println(5.66 - 3.1);
				
				System.out.println(3.1 * 8.4); //En este caso se ha calculado de forma erronea el redondeo del numero
				//Esto se debe a la forma en que se almacenan y manejan los números decimales en el sistema binario de la computadora.
				
				System.out.println(17.0 / 4.0);
			}
		}

}
