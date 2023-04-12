package pkg.entity;
public class Person {
	private int id;
	private String firstname, lastname;
	private int age;
	public Person(int id, String firstname, String lastname, int age) {
		this.id = id > 0
			? id
			: 0;
		this.firstname = !firstname.isBlank()
			? firstname.strip()
			: "";
		this.lastname = !lastname.isBlank()
			? lastname.strip()
			: "";
		this.age = age > 0
			? age
			: 0;
	}
	public int getId() {
		return id;
	}
	public String getFirstname() {
		return firstname;
	}
	public String getLastname() {
		return lastname;
	}
	public int getAge() {
		return age;
	}
	public void setFirstname(String firstname) {
		if (!firstname.isBlank())
			this.firstname = firstname.strip();
	}
	public void setLastname(String lastname) {
		if (!lastname.isBlank())
			this.lastname = lastname.strip();
	}
	public void setAge(int age) {
		if (age > 0)
			this.age = age;
	}
	public Person setPerson(Person p) {
		setFirstname(p.firstname);
		setLastname(p.lastname);
		setAge(p.age);
		return this;
	}
	@Override
	public String toString() {
		return "[%d] Hi! I'm %s %s. I'm %s..".formatted(id, firstname, lastname, age);
	}
}