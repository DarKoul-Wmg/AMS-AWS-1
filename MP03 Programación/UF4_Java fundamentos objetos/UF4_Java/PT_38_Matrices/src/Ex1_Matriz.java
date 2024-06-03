
public class Ex1_Matriz {

	public static void main(String[] args) {
		int matriz[][] =  new int[3][3];
		int relleno = 3;
		for (int i=0;i<matriz.length;i++) {
			for(int j = 0;j<matriz.length;j++) {
				matriz[i][j] = relleno;
				relleno ++;
			}
		}
		System.out.println("Matriz:");
		for (int i=0; i<matriz.length; i++) {
			for (int j=0; j<matriz[0].length; j++) {
				System.out.printf("%5d",matriz[i][j]);
			}
			System.out.println();
		}
		System.out.println("----------------a--------------------");
		
		//A
		for (int i=0; i<matriz.length; i++) {
			for (int j=0; j<matriz[0].length; j++) {
				int valor = matriz[i][j];
				if (valor == 5 || valor == 7 || valor ==9) {
					System.out.println("El valor: "+valor+ " se encuentra en i = "+i +" j = "+j);
				}
			
			}
		}
		//b
		System.out.println("----------------b--------------------");
		System.out.println("Mostrar valores de la matriz por filas: ");
		for (int fila = 0; fila<matriz.length; fila++) {
			for (int i=0; i<matriz.length; i++) {
				System.out.println(matriz[fila][i]);
			}
		}
		//c
		System.out.println("----------------c--------------------");
		System.out.println("Mostrar valores de la matriz por columnas: ");
		for (int columna = 0; columna<matriz.length; columna++) {
			for (int i=0; i<matriz.length; i++) {
				System.out.println(matriz[i][columna]);
			}
		}
		System.out.println("----------------d--------------------");
		System.out.println("Mostrar diagonal de la matriz: ");
		for (int i = 0; i<matriz.length; i++) {
			System.out.println(matriz[i][i]);
			 
		}
	}
}
