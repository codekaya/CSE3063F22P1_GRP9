package CSE3063F22P1_GRP9;

import java.util.ArrayList;

public class Student {
	private String ID;
	private String firstName;
	private String lastName;
	private int semester;
	private Transcript transcript;
	private String advisor;
	private ArrayList<Course> requestedCourses;
	
	Student(){
		requestedCourses = new ArrayList<Course>();
	}

	public String getID() {
		return ID;
	}

	public void setID(String iD) {
		ID = iD;
	}

	public String getFirstName() {
		return firstName;
	}

	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}

	public String getLastName() {
		return lastName;
	}

	public void setLastName(String lastName) {
		this.lastName = lastName;
	}

	public int getSemester() {
		return semester;
	}

	public void setSemester(int semester) {
		this.semester = semester;
	}

	public Transcript getTranscript() {
		return transcript;
	}

	public void setTranscript(Transcript transcript) {
		this.transcript = transcript;
	}

	public String getAdvisor() {
		return advisor;
	}

	public void setAdvisor(String advisor) {
		this.advisor = advisor;
	}

	public ArrayList<Course> getRequestedCourses() {
		return requestedCourses;
	}

	public void setRequestedCourses(ArrayList<Course> requestedCourses) {
		this.requestedCourses = requestedCourses;
	}
	
	public void addRequestedCourse(Course course) {
		this.requestedCourses.add(course);
	}
	
}
