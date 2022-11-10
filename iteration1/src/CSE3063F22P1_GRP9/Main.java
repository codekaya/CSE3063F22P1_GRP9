package CSE3063F22P1_GRP9;

public class Main {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		JsonParser input = new JsonParser();
		RandomStudent randomStudentGenerator = new RandomStudent(input.getFirstNames(),input.getLastNames(),input.getAdvisors(),input.getCourses());
		Student std = randomStudentGenerator.createRandomStudent(2,37);
		OutputJSON output = new OutputJSON();
		output.saveRandomStudent(std);
	}

}
