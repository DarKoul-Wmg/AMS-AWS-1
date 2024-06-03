package pt_Extra;

import java.util.Scanner;

public class ExcepcionesEx3 {

	public static void main(String[] args) {
		//instanciamos la calse apra ejecutar metodos no esatticos
        ExcepcionesEx3 main = new ExcepcionesEx3();
        
        try {
            main.metode1();
        } catch (CaractersNoValids e) {
            System.out.println(e.getMessage());
        }
    }
	
	
	
	public void metode1() throws CaractersNoValids {
        metode2();
    }
	
	
	
    public void metode2() throws CaractersNoValids {
        try {
            metode3();
        } catch (CaractersNoValids e) {
            throw e;
        }
    }
    
    
    public void metode3() throws CaractersNoValids {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introdueix un nom: ");
        String nom = sc.nextLine();


        if (nom.toLowerCase().contains("ñ")) {
            throw new CaractersNoValids("La ñ és un caràcter no vàlid");
            
        } else if (nom.toLowerCase().contains("ç")) {
            throw new CaractersNoValids("La ç és un caràcter no vàlid");
        }
    }

}

class CaractersNoValids extends Exception {
    public CaractersNoValids(String message) {
        super(message);
    }
}
