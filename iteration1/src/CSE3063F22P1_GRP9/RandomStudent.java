package CSE3063F22P1_GRP9;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONValue;

public class RandomStudent {
	private ArrayList<String> names;
	private ArrayList<String> lastNames;
	private ArrayList<String> advisors;
    private ArrayList<ArrayList<Course>> courses;
	RandomStudent(ArrayList<String> names, ArrayList<String> lastNames,ArrayList<String> advisors,ArrayList<ArrayList<Course>> courses){
		this.names = names;
		this.lastNames = lastNames;
		this.advisors = advisors;
		this.courses = courses;
	}
	
	public Student createRandomStudent(int semester,int order) {
		Student student = new Student();
		student.setID(getRandomId(order));
		student.setFirstName(getRandomFirstName());
		student.setLastName(getRandomLastName());
		student.setSemester(semester);
		student.setTranscript(getRandomTranscript(semester,student));
		student.setAdvisor(getRandomAdvisor());
		return student;
	}
	
	private String getRandomId(int order) {
		int Id = 150119000+order;
		return Id+"";
	}
	
	private String getRandomFirstName() {
		return names.get((int)(Math.random()*399));
	}
	
	private String getRandomLastName() {
		return lastNames.get((int)(Math.random()*399));
	}
	
	private String getRandomAdvisor() {
		return advisors.get((int)(Math.random()*6));
	}

	private ArrayList<TakenCourse> simulateGrades(ArrayList<Course> registeredCourses) {
		ArrayList<TakenCourse> takenCourses = new ArrayList<TakenCourse>();
		for(int i = 0;i<registeredCourses.size();i++) {
			TakenCourse takenCourse = new TakenCourse(registeredCourses.get(i),(float) 3.5,"Passed");
			takenCourses.add(takenCourse);
		}
		
		return takenCourses;
	}
	
	private ArrayList<Course> registerRequestedCourses(ArrayList<Course> requestedCourses, ArrayList<SelectionProblem> selectionProblems) {
		return requestedCourses;
	}
	
	private void appendCoursesAtSemester(int semester, ArrayList<Course> requestedCourses) {
		ArrayList<Course> semesterCourses = courses.get(semester-1);
		for(int i = 0;i<semesterCourses.size();i++) {
			requestedCourses.add(semesterCourses.get(i));
		}
	}
}
