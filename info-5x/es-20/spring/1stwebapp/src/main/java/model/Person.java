package model;
public class Person {
	private long id;
	private String firstname, lastname;
	private int age;
	public Person(long id, String firstname, String lastname, int age) {
		this.id = id > 0 ? id : 0;
		this.firstname = !firstname.isBlank() ? firstname.strip() : "(no firstname)";
		this.lastname = !lastname.isBlank() ? lastname.strip() : "(no lastname)";
		this.age = age > 0 ? age : 0;
	}
	public long getId() {
		return this.id;
	}
	public String getFirstname() {
		return this.firstname;
	}
	public String getLastname() {
		return this.lastname;
	}
	public int getAge() {
		return this.age;
	}
	public void setFirstname(String firstname) {
		if(!firstname.isBlank())
			this.firstname = firstname.strip();
	}
	public void setLastname(String lastname) {
		if(!lastname.isBlank())
			this.lastname = lastname.strip();
	}
	public void setAge(int age) {
		if(age > 0)
			this.age = age;
	}
	public void setPerson(Person p) {
		setFirstname(p.firstname);
		setLastname(p.lastname);
		setAge(p.age);
	}
	@Override
	public String toString() {
		return "[%d] Hi, I'm %s %s. I'm %d!..".formatted(id, firstname, lastname, age);
	}	
}