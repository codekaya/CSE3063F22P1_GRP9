package CSE3063F22P1_GRP9;

public class Advisor extends Person{
	private String email;
	private String office;
	
	public Advisor(String ID,String firstName,String lastName,String email,String office) {
		super(ID,firstName,lastName);
		this.email = email;
		this.office = office;
	}
	
	public String getEmail() {
		return email;
	}

	public String getOffice() {
		return office;
	}
}
