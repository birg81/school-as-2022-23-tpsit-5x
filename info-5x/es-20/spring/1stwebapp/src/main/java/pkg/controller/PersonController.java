package pkg.controller;
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
import pkg.entity.Person;
@RestController
@RequestMapping("/api/people")
public class PersonController {
	private ArrayList<Person> people = new ArrayList<>();
	public PersonController() {
		people.add(new Person(1, "Antonio", "Amato", 17));
		people.add(new Person(2, "Barbara", "Boiano", 23));
		people.add(new Person(3, "Ciro", "Cuomo", 18));
		people.add(new Person(4, "Danila", "D'Amato", 19));
	}
	@GetMapping
	public ArrayList<Person> getAll() {
		return people;
	}
	@GetMapping("/{id}") // GET: /10
	public Person getPersonById(@PathVariable int id) {
		return people
			.stream()
			.filter(p -> p.getId() == id)
			.findFirst()
			.orElse(null);
	}
	@GetMapping("/") // GET: /?id=12
	public Person getPersonByIdFromU(@RequestParam int id) {
		return getPersonById(id);
	}
	@PostMapping
	public Person addPerson(@RequestBody Person p) {
		return getPersonById(p.getId()) == null && people.add(p)
			? p
			: null;
	}
	@PutMapping("/{id}")
	public Person updatePerson(@PathVariable int id, @RequestBody Person pDTO) {
		return pDTO != null
			? people
				.stream()
				.filter(p -> p.getId() == id)
				.findFirst()
				.map(p -> p.setPerson(pDTO))
				.orElse(null)
			: null;
	}
	@DeleteMapping("/{id}")
	public Person deletePersonById(@PathVariable int id) {
		Person person = getPersonById(id);
		return people.removeIf(p -> p.getId() == id)
			? person
			: null;
	}
}