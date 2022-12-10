package CSE3063F22P1_GRP9;

import java.util.ArrayList;

public class Transcript {
	private float GPA;
	private int completedCredit;
	private int takenCredit;
	private ArrayList<TakenCourse> takenCourses;
	private ArrayList<SelectionProblem> selectionProblems; 
	
	public Transcript(){
		takenCourses = new ArrayList<TakenCourse>();
		selectionProblems = new ArrayList<SelectionProblem>();
	}
	
	public float getGPA() {
		return GPA;
	}

	public ArrayList<TakenCourse> getTakenCourses() {
		return takenCourses;
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
		 for(int i=0; i<takenCourses.size(); i++){
			if(!takenCourses.get(i).getTakenCourseStatus().equals("Current")) {
				GPA += takenCourses.get(i).getGrade();
			}
		 }
		 GPA = GPA/takenCourses.size();
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

	public void addSelectionProblem(SelectionProblem selectionProblems) {
		this.selectionProblems.add(selectionProblems);
	}
	
	public void setSelectionProblems(ArrayList<SelectionProblem> selectionProblems) {
		this.selectionProblems = selectionProblems;
	}
	
	public TakenCourse findCourse(Course course){
		for(int i = 0;i<takenCourses.size();i++){
			if(takenCourses.get(i).getCourse().getName().equals(course.getName())) {
				return takenCourses.get(i);
			}
		}
		return null;
	}
}