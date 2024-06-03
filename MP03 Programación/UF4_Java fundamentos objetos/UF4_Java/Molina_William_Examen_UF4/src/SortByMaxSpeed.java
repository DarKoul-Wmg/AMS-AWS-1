import java.util.Comparator;

public class SortByMaxSpeed implements Comparator<MotorizedVehicle> {

	public int compare(MotorizedVehicle mv1, MotorizedVehicle mv2) {

		return mv1.getEngine().getMaxSpeed() - mv2.getEngine().getMaxSpeed();
	}

}
