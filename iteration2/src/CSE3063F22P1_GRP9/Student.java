package CSE3063F22P1_GRP9;

import java.util.ArrayList;

public class Student extends Person{
	private int semester;
	private Transcript transcript;
	private Advisor advisor;
	private ArrayList<Course> requestedCourses;

	public Student(String Id,String FName,String LName,int semester,Advisor advisor){
		super(Id,FName,LName);
		requestedCourses = new ArrayList<Course>();
		this.semester = semester;
		this.advisor = advisor;
	}

	public int getSemester() {
		return semester;
	}

	public Transcript getTranscript() {
		return transcript;
	}

	public Advisor getAdvisor() {
		return advisor;
	}

	public ArrayList<Course> getRequestedCourses() {
		return requestedCourses;
	}
	
	public void addRequestedCourse(Course course) {
		this.requestedCourses.add(course);
	}
	
	public void setTranscript(Transcript transcript) {
		this.transcript = transcript;
	}
	
}
