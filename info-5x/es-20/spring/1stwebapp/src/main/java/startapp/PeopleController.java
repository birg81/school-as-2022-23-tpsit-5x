package startapp;
import java.util.ArrayList;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import model.Person;
@RestController
@RequestMapping("/api/people")
public class PeopleController {
	private ArrayList<Person> people;
	public PeopleController() {
		people = new ArrayList<>();
		people.add(new Person(1, "Antonio", "Amato", 17));
		people.add(new Person(2, "Barbara", "Boiano", 23));
		people.add(new Person(3, "Ciro", "Cuomo", 18));
		people.add(new Person(4, "Danila", "D'Amato", 19));
	}
	@GetMapping
	public ArrayList<Person> getAllPeople() {
		return people;
	}
	@GetMapping("/{id}")	// GET: /10
	public Person getPersonById(@PathVariable long id) {
		return people
			.stream()
			.filter(p -> p.getId() == id)
			.findFirst()
			.orElse(null);
	}
	@GetMapping("/")	// GET: /?id=10
	public Person getPersonFromURL(@RequestParam long id) {
		return getPersonById(id);
	}
	@PostMapping
	public Person addPerson(@RequestBody Person p) {
		return (getPersonById(p.getId()) == null && people.add(p))?p:null;
	}
	@PutMapping("/{id}")
	public Person updatePerson(@PathVariable long id, @RequestBody Person pDTO) {
		people
			.stream()
			.filter(p -> p.getId() == id)
			.findFirst()
			.ifPresent(p -> p.setPerson(pDTO));
		return getPersonById(id);
	}
	@DeleteMapping("/{id}")
	public Person deletePersonById(@PathVariable long id) {
		Person person = getPersonById(id);
		return people.removeIf(p -> p.getId() == id) ? person : null;
	}
}