package CSE3063F22P1_GRP9;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.Map;

import org.apache.log4j.Logger;
import org.json.simple.JSONArray;
import org.json.simple.JSONValue;

import com.fasterxml.jackson.databind.ObjectMapper;

public class OutputJSON {
	final Logger logger = Logger.getLogger(OutputJSON.class);
	public void saveStudent(Student student){
		Map map = new LinkedHashMap();
		map.put("ID", student.getID());
		map.put("FirstName",student.getFirstName());
		map.put("LastName",student.getLastName());
		map.put("Semester",student.getSemester()+1);
		map.put("Advisor",student.getAdvisor());
		map.put("Transcript",getTranscriptHashMap(student.getTranscript()));
		map.put("RequestedCourses",student.getRequestedCourses());
		try {
			ObjectMapper mapper = new ObjectMapper();
			String jsonString = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(map);
			File dir = new File("students");
			dir.mkdir();
			FileWriter file = new FileWriter("students/%s.json".formatted(student.getID()));
			file.write(jsonString);
			file.close();
			logger.info("Student json file be created, file name is:" +student.getID()+".json");
		}catch(IOException e) {
			logger.error("Student json file couldn't be created");
			System.exit(3);
		}
	}
	
	private Map getTranscriptHashMap(Transcript transcript) {
		Map map = new LinkedHashMap();
		map.put("GPA", String.format("%.2f", transcript.getGPA()));
		map.put("TakenCredit", transcript.getTakenCredit());
		map.put("CompletedCredit",transcript.getCompletedCredit());
		map.put("TakenCourses",getJSONArrayofTakenCourses(transcript.getTakenCourses()));
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
			map.put("Credit",takenCourse.getCourse().getCredit());
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
	
	public void saveCourseStatistics(ArrayList<ArrayList<Course>> courses,String semester) {
		String allCourseStatistics = "";
		for(int i = 0;i<courses.size();i++) {
			for(int j = 0;j<courses.get(i).size();j++) {
				Course course = courses.get(i).get(j);
				if(!course.getSemester().equals(semester)) continue;
				CourseStatistics courseStatistics = course.getCourseStatistics();
				String s = course.getID()+" "+courses.get(i).get(j).getName()+" Statistics;\n";
				s += "	Percentage of sucessfull registerion:"+ Math.round(courseStatistics.getRateOfSuccessfulRegistration() * 100) +"%\n";
				s += "	Number of registered students:"+courseStatistics.getRegisteredStudentCount()+"\n";
				s += "	Number of registration failures:"+courseStatistics.getRegistrationFailureCount()+"\n";
				s += "	Number of quota problems:"+courseStatistics.getQuotaProblemCount()+"\n";
				s += "	Number of prerequisite problems:"+courseStatistics.getPrerequisiteProblemCount()+"\n";
			
				//System.out.print(s);
				logger.info(s);
				allCourseStatistics += s;
			}
		}
		try {
			FileWriter file = new FileWriter("DepartmentStatistics.txt");
			file.write(allCourseStatistics);
			file.close();
			logger.info("Department Statistics file is created.- DepartmentStatistics.txt");
		} catch (IOException e) {
			logger.error("Department Statistics couldn't be saved");
			System.exit(1);
		}
	}
}