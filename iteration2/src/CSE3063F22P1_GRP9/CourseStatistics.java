package CSE3063F22P1_GRP9;

public class CourseStatistics {
	private int registeredStudentCount;
	private int registrationFailureCount;
	private int quotaProblemCount;
	private int prerequisiteProblemCount;
	
	public void incrRegisteredStudentCount() {
		registeredStudentCount++;
	}
	
	public void incrRegistrationFailureCount() {
		registrationFailureCount++;
	}
	
	public void incrQuotaProblemCount() {
		quotaProblemCount++;
	}
	
	public void incrPrerequisiteProblemCount() {
		prerequisiteProblemCount++;
	}

	public int getRegisteredStudentCount() {
		return registeredStudentCount;
	}

	public int getRegistrationFailureCount() {
		return registrationFailureCount;
	}

	public int getQuotaProblemCount() {
		return quotaProblemCount;
	}

	public int getPrerequisiteProblemCount() {
		return prerequisiteProblemCount;
	}
	
    public double getRateOfSucessfullRegistraion() {
	   return (1.0 * registeredStudentCount)/ (registrationFailureCount + registeredStudentCount);
}
	
}
