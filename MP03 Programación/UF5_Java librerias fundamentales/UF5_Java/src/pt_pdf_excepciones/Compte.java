package pt_pdf_excepciones;

public class Compte {
	
	private float saldo;
	private String nif;

	public Compte(float saldo, String nif) {
	
		this.saldo = saldo;
		this.nif = nif;
	}

	public float getSaldo() {
		return saldo;
	}

	public void setSaldo(float saldo) {
		this.saldo = saldo;
	}
	
	public String getNif() {
		return nif;
	}
	
	
	public void ingressar(float c) {
		float new_saldo = getSaldo() + c;
		
		setSaldo(new_saldo);
	}
	
	//Conforme puede lanzar expeciones
	public void extreure(float c) throws SaldoInsuficienteException{
		
		if (c>this.saldo) {
			throw new SaldoInsuficienteException("Saldo insuficiente para realizar la operación");
		
		} else {
			float new_saldo = getSaldo() - c;
			setSaldo(new_saldo);
		}
	}

	public String toString() {
		return "NIF = " + nif + " Saldo = " + saldo + "\n";
	}	
}
//excepcion personalizada
class SaldoInsuficienteException extends Exception {
	
    public SaldoInsuficienteException(String mensaje) {
        super(mensaje);
    }
    
    public SaldoInsuficienteException(){
		System.out.println("Mensaje de MiExcepcion indeterminado");
		
	}
}


