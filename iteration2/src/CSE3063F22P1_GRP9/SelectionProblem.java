package CSE3063F22P1_GRP9;

public class SelectionProblem {
	private int Id;
	private Course notRegisteredCourse;
	private String description;
	
	public SelectionProblem(Course notRegisteredCourse){
		this.notRegisteredCourse = notRegisteredCourse;
	}
	
	public SelectionProblem(int Id,Course notRegisteredCourse,String description){
		this.Id = Id;
		this.notRegisteredCourse = notRegisteredCourse;
		this.description = description;
	}
	
	public int getId() {
		return Id;
	}

	public Course getNotRegisteredCourse() {
		return notRegisteredCourse;
	}

	public String getDescription() {
		return description;
	}
	
}