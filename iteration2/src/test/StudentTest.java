package test;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import CSE3063F22P1_GRP9.Advisor;
import CSE3063F22P1_GRP9.Student;

class StudentTest {

	@Test
	void ConstructionTest() {
		Advisor sampleAdvisor = new Advisor("109","Paul","Walker","deneme@gmail.com","M2-9");
		Student sampleStudent = new Student("150120000","Jonny","Deep",4,sampleAdvisor);
		
		String expectedAdvisorName = "Paul";
		String AdvisorName = sampleStudent.getAdvisor().getFirstName(); 
		
		Assertions.assertEquals(expectedAdvisorName,AdvisorName);
	}

}
