package CSE3063F22P1_GRP9;

import org.apache.log4j.Logger;

public class Main {

	public static void main(String[] args){
		final Logger logger = Logger.getLogger(Main.class);
		logger.info("Simulation is starting");
		CourseRegistrationSimulation simulation = new CourseRegistrationSimulation();
		simulation.startSimulation();
		logger.info("Course registration simulation ended.");
	}
}