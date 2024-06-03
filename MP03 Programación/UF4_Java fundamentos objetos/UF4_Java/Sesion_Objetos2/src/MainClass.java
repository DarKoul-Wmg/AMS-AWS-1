
public class MainClass {

	public static void main(String[] args) {
		
//		Alumno paco = new Alumno("11111111H","Paco","Gonzalez");
//		Alumno samantha = new Alumno("22222222A","Samantha","Sanchez");
//		System.out.println(paco);
		
		Personas[] instituto = new Personas[8];
		instituto[0] = new Alumno("11111111H","Paco","Gonzalez");
		instituto[1] = new Alumno("22222222A","Samantha","Sanchez");
		instituto[2] = new Alumno("33333333B","Sandra","Gomez");
		instituto[3] = new Alumno("44444444H","Sergio","Rodriguez");
		instituto[4] = new Alumno("55555555N","Sebastian","Garcia");
		instituto[5] = new PersonalServicio("66666666N","Pepe","Santacana","Limpieza");
		instituto[6] = new PersonalServicio("77777777N","Sara","Lara","Limpieza");
		String[] modulos = {"M3","M4"};
		instituto[7] = new Profesor("88888888N","Jordi","Garci","Tutor",modulos);
		

		// ALUMNOS
		for (int i = 0; i<instituto.length;i++) {
			
			if (instituto[i].getClass().getCanonicalName().equals("Alumno"))
			System.out.println(instituto[i]);
		}
		System.out.println("\n**************\n");
		
		// PERSONAL
		for (int i = 0; i<instituto.length;i++) {
					
			if (instituto[i].getClass().getCanonicalName().equals("PersonalServicio"))
			System.out.println(instituto[i]);
		}
		System.out.println("\n**************\n");
		
		//PROFESOR
		for (int i = 0; i<instituto.length;i++) {
			
			if (instituto[i].getClass().getCanonicalName().equals("Profesor"))
			System.out.println(instituto[i]);
		}
		System.out.println("\n**************\n");
		
		
		
		//PersonalServicio pepe = new PersonalServicio("66666666N","Pepe","Santacana","Limpieza");
//		System.out.println(pepe);
//		System.out.println(Personas.variable);
		
//		pepe.setNombre("Jaime");
//		System.out.println(pepe);
//		Personas.Saludar();
		
//		System.out.println(pepe.getClass().getCanonicalName()); //pepe.getClass().getCanonicalName() me dice a que clase pertenece
//		System.out.println(pepe instanceof Object); //todo hereda de Object (super)
		
	}
}
