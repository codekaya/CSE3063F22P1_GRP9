package CSE3063F22P1_GRP9;

public abstract class Person {
	private String ID;
	private String firstName;
	private String lastName;
	
	public Person(String ID,String firstName,String lastName) {
		this.ID = ID;
		this.firstName = firstName;
		this.lastName = lastName; 
	}
	
	public abstract void status();
	public String getID() {
		return ID;
	}

	public String getFirstName() {
		return firstName;
	}

	public String getLastName() {
		return lastName;
	}
}
