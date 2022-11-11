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
	
	public Student createRandomStudent(int semester) {
		Student student = new Student();
		student.setID(getRandomId());
		student.setFirstName(getRandomFirstName());
		student.setLastName(getRandomLastName());
		student.setSemester(semester);
		student.setTranscript(getRandomTranscript(semester,student));
		student.setAdvisor(getRandomAdvisor());
		return student;
	}
	
	private String getRandomId() {
		return "150119037";
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
	
	private Transcript getRandomTranscript(int semester,Student student) {
		Transcript transcript = new Transcript();
		String currentSemester = "Fall";
		String nextSemester = "Spring";
		for(int i = 1;i<=semester+1;i++) {
			student.setRequestedCourses(new ArrayList<Course>());
			ArrayList<TakenCourse> takenCourses = transcript.getTakenCourses();
			ArrayList<SelectionProblem> selectionProblems = transcript.getSelectionProblems();
			for(int j = 0;j<takenCourses.size();j++) {
				TakenCourse takenCourse = takenCourses.get(j);
				String s = takenCourse.getCourse().getSemester();
				if(takenCourse.getTakenCourseStatus()=="failed" && (s.equals(currentSemester) ||s.equals("Both"))) {
					student.addRequestedCourse((takenCourse.getCourse()));
				}
			}
			for(int j = 0;j<selectionProblems.size();j++) {
				Course notRegisteredCourse = selectionProblems.get(j).getNotRegisteredCourse();
				if(notRegisteredCourse.getSemester().equals(currentSemester)) {
					student.addRequestedCourse(notRegisteredCourse);
				}
			}	
			appendCoursesAtSemester(i,student.getRequestedCourses());
			if(i-1 == semester) {
				break;
			}
			ArrayList<Course> registeredCourses = registerRequestedCourses(student.getRequestedCourses(),selectionProblems);
			//Register fail olursa transkripte register problem diye ekleyelim ve requested course başta bunlarıda ekleyelim
			ArrayList<TakenCourse> simulatedGrades = simulateGrades(registeredCourses);
			for(int k = 0;k<simulatedGrades.size();k++) {
				transcript.addTakenCourse(simulatedGrades.get(k));//Transkriptte aynı dersten varsa sadece status ve grade güncellenmeli.
			}
			String temp = currentSemester;
			currentSemester=nextSemester;
			nextSemester=temp;
		}
		transcript.setSelectionProblems(new ArrayList<SelectionProblem>());
		return transcript;
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