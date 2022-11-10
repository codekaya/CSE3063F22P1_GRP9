package CSE3063F22P1_GRP9;

import java.io.FileReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.Iterator;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class JsonParser {
	//Basitleştirdim sadece courseları çekicek 
	private JSONObject input;
	private ArrayList<ArrayList<Course>> courses;
	public JsonParser() throws Exception{
		Reader reader = new FileReader("input.json");
		JSONParser parser = new JSONParser();
		this.input = (JSONObject) parser.parse(reader);
		courses = new ArrayList<ArrayList<Course>>();
		readCourses();
	}

}