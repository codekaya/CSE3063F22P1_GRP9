package CSE3063F22P1_GRP9;

import java.util.ArrayList;
import java.util.List;

public class Transcript {
	private float GPA;
	private ArrayList<TakenCourse> takenCourses;
	private int completedCredit;
	private int takenCredit;
	private ArrayList<SelectionProblem> selectionProblems; 
	Transcript(){
		takenCourses = new ArrayList<TakenCourse>();
		selectionProblems = new ArrayList<SelectionProblem>();
		setTakenCredit(0);
		completedCredit = 0;
		GPA = 0;
	}
	
	public float getGPA() {
		return GPA;
	}

	public ArrayList<TakenCourse> getTakenCourses() {
		return takenCourses;
	}
	//!!!!!!!!!!!!!!!!!!!GPA completed credit ve taken credit güncellenmeli gpa noktadan sonra 2 hane olacak.
	
	private void calculateGpa() {
		
	}
	public int getCompletedCredit() {
		return completedCredit;
	}

	public int getTakenCredit() {
		return takenCredit;
	}

	public void setTakenCredit(int takenCredit) {
		this.takenCredit = takenCredit;
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
}