package test;

import static org.junit.jupiter.api.Assertions.*;

import org.json.simple.JSONObject;
import org.junit.jupiter.api.Test;

import CSE3063F22P1_GRP9.InputJSON;
import CSE3063F22P1_GRP9.RandomStudent;
import CSE3063F22P1_GRP9.Student;

class RandomStudentTest {

	@Test
	void CreateRandomStudentTest() {
		
		 
		InputJSON input = new InputJSON();
		RandomStudent r1 = new RandomStudent(input);
		Student s = r1.createRandomStudent(4, 6);
		boolean isStudentObjectExist = (s != null);
		assertEquals(isStudentObjectExist, true);
		
		
		
	}

}
