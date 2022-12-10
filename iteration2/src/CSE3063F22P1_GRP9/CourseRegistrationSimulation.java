package CSE3063F22P1_GRP9;

import java.util.ArrayList;

import org.apache.log4j.Logger;

public class CourseRegistrationSimulation {
	final Logger logger = Logger.getLogger(CourseRegistrationSimulation.class);
	public void startSimulation(){
		InputJSON input = new InputJSON();
		ArrayList<Student> students = generateStudents(input);
		
		CourseRegistrationSystem registirationSystem = new CourseRegistrationSystem(input.getSemester());
		for (Student student : students) {
			registirationSystem.registerStudent(student);
		}
		logger.info("Students registiration completed");
		OutputJSON output = new OutputJSON();
		for (Student student : students) {
			output.saveStudent(student);
		}
		output.saveCourseStatistics(input.getCourses(),input.getSemester());
		logger.info("Students saved to the json files");
	}
	
	public ArrayList<Student> generateStudents(InputJSON input){
		RandomStudent randomStudent = new RandomStudent(input);
		ArrayList<Student> students = new ArrayList<Student>();
		String semester = input.getSemester();
		int startingSemester = 0;
		if(semester.equals("Spring"))
			startingSemester++;
		int order = 0;
		int numberOfStudents = input.getNumberOfStudents();
		for(int j = 0;j<numberOfStudents/4;j++) {	
			for(int i = startingSemester;i<8;i+=2) {
				students.add(randomStudent.createRandomStudent(i,order));
				order++;
			}
		}
		logger.info(numberOfStudents+" Random student created");
		return students;
	}
}
