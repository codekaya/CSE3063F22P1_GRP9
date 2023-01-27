package CSE3063F22P1_GRP9;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties({"prerequisite","quota","semester","courseStatistics"})
public class Course {
	private String ID;
	private String name;
	private String prerequisiteId;
	private Course prerequisite;
	private CourseStatistics courseStatistics;
	private int quota;
	private int credit;
	private String semester;
	
	public Course() {
		courseStatistics = new CourseStatistics();
	}
	
	public String getID() {
		return ID;
	}
	public void setID(String id) {
		ID = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Course getPrerequisite() {
		return prerequisite;
	}
	public void setPrerequisite(Course prerequisite) {
		this.prerequisite = prerequisite;
	}
	public String getPrerequisiteId() {
		return prerequisiteId;
	}
	public void setPrerequisiteId(String prerequisiteId) {
		this.prerequisiteId = prerequisiteId;
	}
	public int getQuota() {
		return quota;
	}
	public void setQuota(int quota) {
		this.quota = quota;
	}
	
	public int getCredit() {
		return credit;
	}
	public void setCredit(int credit) {
		this.credit = credit;
	}
	
	public String getSemester() {
		return semester;
	}
	public void setSemester(String semester) {
		this.semester = semester;
	}

	public CourseStatistics getCourseStatistics() {
		return courseStatistics;
	}
	
}