package CSE3063F22P1_GRP9;

public class SelectionProblem {
	private int Id;
	private Course notRegisteredCourse;
	private String description;
	
	public int getId() {
		return Id;
	}
	public void setId(int id) {
		Id = id;
	}
	public Course getNotRegisteredCourse() {
		return notRegisteredCourse;
	}
	public void setNotRegisteredCourse(Course notRegisteredCourse) {
		this.notRegisteredCourse = notRegisteredCourse;
	}
	public String getDescription() {
		return description;
	}
	public void setDescription(String description) {
		this.description = description;
	}	
}
