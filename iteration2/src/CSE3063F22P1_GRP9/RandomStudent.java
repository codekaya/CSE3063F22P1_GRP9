package CSE3063F22P1_GRP9;

import java.util.ArrayList;
import java.util.Random;

public class RandomStudent {
	private InputJSON input;
	RandomStudent(InputJSON input){
		this.input = input;
	}
	
	public Student createRandomStudent(int semester,int order) {
		String Id = getRandomId(semester, order);
		String FName = getRandomFirstName();
		String LName = getRandomLastName();
		Advisor advisor = getRandomAdvisor();
		Student student = new Student(Id,FName,LName,semester,advisor);
		createStudentTranscript(semester,student);
		return student;
	}
	
	private String getRandomId(int semester, int order) {
		int Id = 150118000+order;
		Id += 4000 - (Math.floor((semester+1)/2)*1000);
		return Id+"";
	}
	
	private String getRandomFirstName() {
		return input.getFirstNames().get((int)(Math.random()*399));
	}
	
	private String getRandomLastName() {
		return input.getLastNames().get((int)(Math.random()*399));
	}
	
	private Advisor getRandomAdvisor() {
		return input.getAdvisors().get(0);
	}
	
	private void createStudentTranscript(int semester,Student student) {
		Transcript transcript = new Transcript(student);
		String currentSemester = "Fall";
		String nextSemester = "Spring";
		ArrayList<SelectionProblem> selectionProblems = new ArrayList<SelectionProblem>();
		ArrayList<Course> requestedCourses = new ArrayList<Course>();
		for(int i = 1;i<=semester+1;i++) {
			requestedCourses.clear();
			ArrayList<TakenCourse> takenCourses = transcript.getTakenCourses();
			for(int j = 0;j<takenCourses.size();j++) {
				TakenCourse takenCourse = takenCourses.get(j);
				String s = takenCourse.getCourse().getSemester();
				if(takenCourse.getTakenCourseStatus()=="Failed" && (s.equals(currentSemester) ||s.equals("Both"))) {
					requestedCourses.add(takenCourse.getCourse());
				}
			}
			for(int j = 0;j<selectionProblems.size();j++) {
				Course notRegisteredCourse = selectionProblems.get(j).getNotRegisteredCourse();
				if(notRegisteredCourse.getSemester().equals(currentSemester)) {
					requestedCourses.add(notRegisteredCourse);
				}
			}	
			appendCoursesAtSemester(i,requestedCourses);
			if(i-1 == semester) {
				break;
			}
			ArrayList<Course> registeredCourses = registerRequestedCourses(requestedCourses,transcript);
			ArrayList<TakenCourse> simulatedGrades = simulateGrades(registeredCourses);
			for(int k = 0;k<simulatedGrades.size();k++) {
				transcript.addTakenCourse(simulatedGrades.get(k));
			}
			String temp = currentSemester;
			currentSemester=nextSemester;
			nextSemester=temp;
		}
		student.setTranscript(transcript);
		for (Course course : requestedCourses) {
			student.addRequestedCourse(course);
		}
	}

	private ArrayList<TakenCourse> simulateGrades(ArrayList<Course> registeredCourses) {
		double probabilityOfPassingCourse = input.getProbabilityOfPassingCourse();
		ArrayList<TakenCourse> takenCourses = new ArrayList<TakenCourse>();
		for(int i = 0;i<registeredCourses.size();i++) {
			String status = "Passed";
			float grade = 1;
			Random p = new Random();
			if(p.nextDouble()>probabilityOfPassingCourse)
				status = "Failed";
			else
				grade = p.nextInt(3)+2;
			TakenCourse takenCourse = new TakenCourse(registeredCourses.get(i),grade,status);
			takenCourses.add(takenCourse);
		}
		return takenCourses;
	}
	
	private ArrayList<Course> registerRequestedCourses(ArrayList<Course> requestedCourses, Transcript transcript) {
		ArrayList<Course> registeredCourses = new ArrayList<Course>();
		for (Course course : requestedCourses) {
			if(course.getPrerequisite()==null) {
				registeredCourses.add(course);
				continue;
			}
			TakenCourse prerequisiteInTranscript = transcript.findCourse(course.getPrerequisite());
			if(prerequisiteInTranscript==null || !prerequisiteInTranscript.getTakenCourseStatus().equals("Passed")) {
				SelectionProblem sp = new SelectionProblem(course);
				transcript.addSelectionProblem(sp);
			}
			else {
				registeredCourses.add(course);
			}		
		}
		return registeredCourses;
	}
	
	private void appendCoursesAtSemester(int semester, ArrayList<Course> requestedCourses) {
		ArrayList<Course> semesterCourses = input.getCourses().get(semester-1);
		for(int i = 0;i<semesterCourses.size();i++) {
			requestedCourses.add(semesterCourses.get(i));
		}
	}
}
