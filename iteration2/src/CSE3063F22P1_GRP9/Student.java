package CSE3063F22P1_GRP9;

import java.util.ArrayList;

public class Student extends Person{
	private int semester;
	private Transcript transcript;
	private Advisor advisor;
	private ArrayList<Course> requestedCourses;

	Student(){
		requestedCourses = new ArrayList<Course>();
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

	public Advisor getAdvisor() {
		return advisor;
	}

	public void setAdvisor(Advisor advisor) {
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
