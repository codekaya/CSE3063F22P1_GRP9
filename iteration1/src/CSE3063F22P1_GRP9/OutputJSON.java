package CSE3063F22P1_GRP9;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONValue;

public class OutputJSON {

	public void saveStudent(Student student) throws IOException {
		Map map = new LinkedHashMap();
		map.put("ID", student.getID());
		map.put("FirstName",student.getFirstName());
		map.put("LastName",student.getLastName());
		map.put("Semester",student.getSemester()+1);
		map.put("Transcript",getTranscriptHashMap(student.getTranscript()));
		map.put("Advisor",student.getAdvisor());
		map.put("RequestedCourses",getRequestedCoursesHashMap(student.getRequestedCourses()));
		String jsonText = JSONValue.toJSONString(map);
		File dir = new File("students");
		dir.mkdir();
		FileWriter file = new FileWriter("students/%s.json".formatted(student.getID()));
		file.write(jsonText);
		file.close();

	}

	private Map getTranscriptHashMap(Transcript transcript) {
		Map map = new LinkedHashMap();
		map.put("GPA", String.format("%.2f", transcript.getGPA()));
		map.put("TakenCourses",getJSONArrayofTakenCourses(transcript.getTakenCourses()));
		map.put("CompletedCredit",transcript.getCompletedCredit());
		map.put("TakenCredit", transcript.getTakenCredit());
		map.put("RegistirationProblems",getJSONArrayOfSelectionProblems(transcript.getSelectionProblems()));
		return map;
	}

	private Object getJSONArrayofTakenCourses(ArrayList<TakenCourse> takenCourses) {
		JSONArray takenCoursesMap = new JSONArray();
		for(int i = 0;i<takenCourses.size();i++) {
			Map map = new LinkedHashMap();
			TakenCourse takenCourse = takenCourses.get(i);
			map.put("CourseId",takenCourse.getCourse().getID());
			map.put("CourseName",takenCourse.getCourse().getName());
			map.put("takenCourseStatus",takenCourse.getTakenCourseStatus());
			map.put("Grade",takenCourse.getGrade());
			takenCoursesMap.add(map);
		}
		return takenCoursesMap;
	}

	private JSONArray getJSONArrayOfSelectionProblems(ArrayList<SelectionProblem> selectionProblems) {
		JSONArray selectionProblemsMap = new JSONArray();
		for(int i = 0;i<selectionProblems.size();i++) {
			Map map = new LinkedHashMap();
			SelectionProblem problem = selectionProblems.get(i);
			map.put("ProblemId",problem.getId());
			map.put("Course",problem.getNotRegisteredCourse().getName());
			map.put("Reason",problem.getDescription());
			selectionProblemsMap.add(map);
		}
		return selectionProblemsMap;
	}
	
	private JSONArray getRequestedCoursesHashMap(ArrayList<Course> requestedCourses) {
		JSONArray requestedCoursesMap = new JSONArray();
		for (int i = 0; i < requestedCourses.size(); i++) {
			Map map = new LinkedHashMap();
			Course reqCourse = requestedCourses.get(i);
			map.put("CourseId", reqCourse.getID());
			map.put("CourseName",reqCourse.getName());
			requestedCoursesMap.add(map);
		}
		return requestedCoursesMap;
	}
}