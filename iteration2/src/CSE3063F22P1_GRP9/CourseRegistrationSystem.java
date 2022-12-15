
package CSE3063F22P1_GRP9;

import java.util.ArrayList;

public class CourseRegistrationSystem {
	private String semester;
	private final int MAX_COURSE_COUNT;  
	CourseRegistrationSystem(String semester){
		this.semester = semester;
		MAX_COURSE_COUNT = 10;
	}
	
	public void registerStudent(Student student) {
		Transcript transcript = student.getTranscript();
		ArrayList<Course> requestedCourses = student.getRequestedCourses();
		int coursesTaken = 0;
		for (Course course : requestedCourses) {
			if(!course.getSemester().equals(semester)) {
				course.getCourseStatistics().incrRegistrationFailureCount();
				String description = "Course is not available at "+semester;
				SelectionProblem problem = new SelectionProblem(0,course,description);
				transcript.addSelectionProblem(problem);
				continue;
			}
			Course prerequisite = course.getPrerequisite();
			if(prerequisite!=null) {
				TakenCourse prerequisiteInTranscript = transcript.findCourse(prerequisite);
				if(prerequisiteInTranscript==null || !prerequisiteInTranscript.getTakenCourseStatus().equals("Passed")) {
					course.getCourseStatistics().incrPrerequisiteProblemCount();
					course.getCourseStatistics().incrRegistrationFailureCount();
					String description = "Prerequisite "+prerequisite.getName()+" isn't passed";
					SelectionProblem problem = new SelectionProblem(1,course,description);
					transcript.addSelectionProblem(problem);
					continue;
				}
			}
			if(course.getQuota()<1) {
				course.getCourseStatistics().incrQuotaProblemCount();
				course.getCourseStatistics().incrRegistrationFailureCount();
				String description = "The quota is exceeded.";
				SelectionProblem problem = new SelectionProblem(2,course,description);
				transcript.addSelectionProblem(problem);
				continue;
			}
			if(coursesTaken>MAX_COURSE_COUNT) {
				course.getCourseStatistics().incrRegistrationFailureCount();
				String description = "Student can't take more than 10 courses at one semester.";
				SelectionProblem problem = new SelectionProblem(3,course,description);
				transcript.addSelectionProblem(problem);
				continue;
			}
			if(course.getID().equals("CSE4297") && student.getTranscript().getCompletedCredit()<165) {
				course.getCourseStatistics().incrRegistrationFailureCount();
				String description = "Student should have completed more than 165 credit to enroll CSE4297";
				SelectionProblem problem = new SelectionProblem(4,course,description);
				transcript.addSelectionProblem(problem);
				continue;
			}
			if(course.getID().equals("TExxx") && student.getTranscript().getCompletedCredit()<155) {
				course.getCourseStatistics().incrRegistrationFailureCount();
				String description = "Student should have completed more than 155 credit to enroll Technical Elective Courses";
				SelectionProblem problem = new SelectionProblem(4,course,description);
				transcript.addSelectionProblem(problem);
				continue;
			}
			course.getCourseStatistics().incrRegisteredStudentCount();
			TakenCourse takenCourse = new TakenCourse(course,0,"Current");
			transcript.addTakenCourse(takenCourse);
			course.setQuota(course.getQuota()-1);
			coursesTaken++;
		}
		
	}
	
}