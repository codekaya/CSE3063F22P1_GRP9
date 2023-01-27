package test;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import CSE3063F22P1_GRP9.Advisor;
import CSE3063F22P1_GRP9.Course;
import CSE3063F22P1_GRP9.Student;
import CSE3063F22P1_GRP9.TakenCourse;
import CSE3063F22P1_GRP9.Transcript;

class TranscriptTest {

	@Test
void calculateGpaTest() {
		
		Course s1 = new Course();
		s1.setName("ATA121");
		s1.setCredit(10);
	    TakenCourse t1 = new TakenCourse(s1,3,"Passed");
	    
		
		Course s2 = new Course();
		s2.setName("MBG1201");
		s2.setCredit(5);
	    TakenCourse t2 = new TakenCourse(s2,3,"Passed");
	    
	    Advisor a1 = new Advisor("10","Lionel","Messi","deneme@gmail.com","M2-9");
		Student st1 = new Student("7","Cristiano","Ronaldo",4,a1);
		
	    float expectedGPA = 45 / 15;
	    
	    Transcript testT = new Transcript(st1);
	    testT.addTakenCourse(t1);
	    testT.addTakenCourse(t2);
	    
	    assertEquals(expectedGPA, testT.getGPA());
	    
	    
	    
	    

		
		
		
	}


}
