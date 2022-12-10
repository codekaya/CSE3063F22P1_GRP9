package CSE3063F22P1_GRP9;

public class TakenCourse {
	private Course course;
	private String takenCourseStatus;
	private float grade;
	
	public TakenCourse(Course course,float grade,String takenCourseStatus){
		this.course = course;
		this.grade = grade;
		this.takenCourseStatus = takenCourseStatus;
	}

	public Course getCourse() {
		return course;
	}

	public void setCourse(Course course) {
		this.course = course;
	}

	public String getTakenCourseStatus() {
		return takenCourseStatus;
	}

	public void setTakenCourseStatus(String takenCourseStatus) {
		this.takenCourseStatus = takenCourseStatus;
	}

	public float getGrade() {
		return grade;
	}

	public void setGrade(float grade) {
		this.grade = grade;
	}
	
}