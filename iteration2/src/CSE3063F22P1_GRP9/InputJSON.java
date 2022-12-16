package CSE3063F22P1_GRP9;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.Iterator;

import org.apache.log4j.Logger;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class InputJSON {
	final Logger logger = Logger.getLogger(InputJSON.class);
	private JSONObject input;
	private ArrayList<ArrayList<Course>> courses;
	public InputJSON(){
		try {
			Reader reader = new FileReader("parameters.json");
			JSONParser parser = new JSONParser();
			this.input = (JSONObject) parser.parse(reader);
			courses = new ArrayList<ArrayList<Course>>();
		}catch(FileNotFoundException e) {
			logger.error("parameters.json file isn't found.");
			System.exit(1);
		}catch(Exception e) {
			logger.error("parameters.json file found, there is another issue:");
			e.printStackTrace();
			System.exit(2);
		}
		readCourses();
	}

	private void readCourses(){
		JSONObject coursesJSON = (JSONObject) input.get("courses");
		for(int i = 1;i<9;i++) {
			ArrayList<Course> semesterCourses = new ArrayList<Course>();
			JSONArray semester = (JSONArray)coursesJSON.get("s"+i);
			Iterator<JSONObject> iterator = semester.iterator();
			while (iterator.hasNext()) {
                Course c = getCourseObject(iterator.next());
                semesterCourses.add(c);
            }
			courses.add(semesterCourses);	
		}
		for(int i = 0;i<courses.size();i++) {
			for(int j = 0;j<courses.get(i).size();j++) {
				Course currCourse = courses.get(i).get(j);
				if(currCourse.getPrerequisiteId()!=null) {;
					currCourse.setPrerequisite(findCourse(currCourse.getPrerequisiteId()));
				}
			}
		}
		logger.info("Courses read from inputJSON.");
	}
	private Course getCourseObject(JSONObject courseJSON){
		Course course = new Course();
		course.setID(courseJSON.get("Course Code").toString());
		course.setName(courseJSON.get("Course Name").toString());
		if(courseJSON.get("Prerequisite")!=null) {
			course.setPrerequisiteId(courseJSON.get("Prerequisite").toString());
		}
		course.setQuota(Integer.parseInt(courseJSON.get("Quota").toString()));
		course.setCredit(Integer.parseInt(courseJSON.get("Credit").toString()));
		course.setSemester(courseJSON.get("Semester").toString());
		return course;
	}
	
	private Course findCourse(String courseId) {
		for(int i = 0;i<courses.size();i++) {
			for(int j = 0;j<courses.get(i).size();j++) {;
				if(courses.get(i).get(j).getID().equals(courseId))
					logger.info("course found");
					return courses.get(i).get(j);
			}
		}
		return null;
	}

	public ArrayList<String> getFirstNames() {
		ArrayList<String> names = new ArrayList<String>();
		JSONArray namesJSON =(JSONArray)input.get("firstNames");
		Iterator<String> iterator = namesJSON.iterator();
		while (iterator.hasNext()) {
            names.add(iterator.next());
        };
        return names;
	}
	
	public ArrayList<String> getLastNames(){
		ArrayList<String> lastNames = new ArrayList<String>();
		JSONArray lastNamesJSON =(JSONArray)input.get("lastNames");
		Iterator<String> iterator = lastNamesJSON.iterator();
		while (iterator.hasNext()) {
            lastNames.add(iterator.next());
        };
        return lastNames;
	}
	
	public ArrayList<Advisor> getAdvisors(){
		ArrayList<Advisor> advisors = new ArrayList<Advisor>();
		JSONArray advisorsJSON =(JSONArray)input.get("advisors");
		Iterator<JSONObject> iterator = advisorsJSON.iterator();
		while (iterator.hasNext()) {
			JSONObject advisorJSON = (JSONObject)iterator.next();
			String FName = advisorJSON.get("firstName").toString();
			String LName = advisorJSON.get("lastName").toString();
			String Id = advisorJSON.get("id").toString();
			String email = advisorJSON.get("email").toString();
			String office = advisorJSON.get("office").toString();
			Advisor advisor = new Advisor(Id,FName,LName,email,office);
            advisors.add(advisor);
        };
        return advisors;
	};
	
	public ArrayList<ArrayList<Course>> getCourses() {
		return courses;
	}
	
	public String getSemester() {
		return input.get("semester").toString();
	}
	
	public int getNumberOfStudents() {
		return Integer.parseInt(input.get("numberOfStudents").toString());
	}
	
	public double getProbabilityOfPassingCourse() {
		return Double.parseDouble(input.get("probabilityOfPassingCourse").toString());
	}
}
