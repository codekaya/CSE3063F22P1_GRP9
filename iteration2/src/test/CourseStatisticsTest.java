package test;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import CSE3063F22P1_GRP9.CourseStatistics;


class CourseStatisticsTest {
	
	private int registeredStudentCount;
	private int registrationFailureCount;
	private double rateOfSucessfullRegistraion;
	@Test
	void getRateOfSucessfullRegistraion() {
		
		
		CourseStatistics csTesting= new CourseStatistics();
		int i;
		for(i=0;i<5;i++) {
		csTesting.incrRegisteredStudentCount();
		
		}
		
		for(i=0;i<1;i++) {
			csTesting.incrRegistrationFailureCount();
			
			}
		
		registeredStudentCount=	csTesting.getRegisteredStudentCount();
		registrationFailureCount = csTesting.getRegistrationFailureCount();
		
		
		
		rateOfSucessfullRegistraion=(1.0 * registeredStudentCount)/ (registrationFailureCount + registeredStudentCount);
	    
	    
	    
		assertEquals(rateOfSucessfullRegistraion,csTesting.getRateOfSucessfullRegistraion());
		
	}
}
