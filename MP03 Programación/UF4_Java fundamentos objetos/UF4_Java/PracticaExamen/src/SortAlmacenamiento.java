import java.util.Comparator;

public class SortAlmacenamiento implements Comparator<Dispositivo>{

	
	public int compare(Dispositivo d1, Dispositivo d2) {
	
		return d1.getDiskCapacity() - d2.getDiskCapacity();
		
	}

}
