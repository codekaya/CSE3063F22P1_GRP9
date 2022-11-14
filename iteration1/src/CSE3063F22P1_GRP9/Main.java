package CSE3063F22P1_GRP9;


import java.util.ArrayList;

public class Main {

	public static void main(String[] args) throws Exception{
		JsonParser input = new JsonParser();
		RandomStudent randomStudent = new RandomStudent(input.getFirstNames(),input.getLastNames(),input.getAdvisors(),input.getCourses());
		
		ArrayList<Student> students = new ArrayList<Student>();
		String semester = input.getSemester();
		int startingSemester = 0;
		if(semester.equals("Spring"))
			startingSemester++;
		int order = 0;
		for(int j = 0;j<100;j++) {	
			for(int i = startingSemester;i<8;i+=2) {
				students.add(randomStudent.createRandomStudent(i,order));
				order++;
			}
		}
		
		CourseRegistirationSystem registirationSystem = new CourseRegistirationSystem(semester);
		for (Student student : students) {
			registirationSystem.registerStudent(student);
		}
		
	
		OutputJSON output = new OutputJSON();
		output.saveStudent(students.get(3));
		output.saveStudent(students.get(2));
		output.saveStudent(students.get(1));
		output.saveStudent(students.get(0));
		/*output.saveStudent(students.get(3));
		output.saveStudent(students.get(1));
		for (Student student : students) {
			output.saveStudent(student);
		}*/
	}
}
