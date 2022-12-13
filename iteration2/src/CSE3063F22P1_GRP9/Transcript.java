package CSE3063F22P1_GRP9;

import java.util.ArrayList;

public class Transcript {
	private Student student;
	private float GPA;
	private int completedCredit;
	private int takenCredit;
	private ArrayList<TakenCourse> takenCourses;
	private ArrayList<SelectionProblem> selectionProblems; 
	
	public Transcript(Student student){
		this.student = student;
		takenCourses = new ArrayList<TakenCourse>();
		selectionProblems = new ArrayList<SelectionProblem>();
	}

	public void addTakenCourse(TakenCourse takenCourse) {
		String status = takenCourse.getTakenCourseStatus();
		int credit = takenCourse.getCourse().getCredit();
		TakenCourse takenCourseInTranscript = findCourse(takenCourse.getCourse());
		if(takenCourseInTranscript==null) {
			takenCourses.add(takenCourse);
			takenCredit += credit;
			if(status.equals("Passed")) {
				completedCredit += credit;
			}
		}
		else {
			if(status.equals("Passed")) {
				completedCredit += credit;
			}
			takenCourseInTranscript.setGrade(takenCourse.getGrade());
			takenCourseInTranscript.setTakenCourseStatus(takenCourse.getTakenCourseStatus());
		}
		calculateGpa();
	}
	
	private void calculateGpa() {
		 GPA = 0;
		 int totalCredit = 0;
		 for(int i=0; i<takenCourses.size(); i++){
			 TakenCourse takenCourse = takenCourses.get(i);
			if(!takenCourse.getTakenCourseStatus().equals("Current")) {
				int credit = takenCourse.getCourse().getCredit();
				GPA += takenCourse.getGrade()*credit;
				totalCredit += credit; 
			}
		 }
		 GPA = GPA/totalCredit;
	}
	
	public TakenCourse findCourse(Course course){
		for(int i = 0;i<takenCourses.size();i++){
			if(takenCourses.get(i).getCourse().getName().equals(course.getName())) {
				return takenCourses.get(i);
			}
		}
		return null;
	}
	
	public int getCompletedCredit() {
		return completedCredit;
	}

	public int getTakenCredit() {
		return takenCredit;
	}
	
	public ArrayList<SelectionProblem> getSelectionProblems() {
		return selectionProblems;
	}

	public void addSelectionProblem(SelectionProblem selectionProblem) {
		this.selectionProblems.add(selectionProblem);
	}
	
	public float getGPA() {
		return GPA;
	}

	public ArrayList<TakenCourse> getTakenCourses() {
		return takenCourses;
	}
	
}