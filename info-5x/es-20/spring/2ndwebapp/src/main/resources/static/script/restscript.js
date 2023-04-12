'use strict';
const personList = async () => await fetch('./api/people')
	.then(res => res.json())
	.catch(e => console.err(e))
	.then(j => j.length === 0 ? j : j.sort((p1, p2) => (p1.lastname > p2.lastname) ? 1 : -1));

const people = async () => {
	document.querySelector('#buddylist').innerHTML = (await personList()).map( p =>
		`
		<tr>
		<td id="id_${p.id}" class="btn-delete" onclick="removePerson(${p.id})"></td>
		<td id="firstname_${p.id}">${p.firstname}</td>
		<td id="lastname_${p.id}">${p.lastname}</td>
		<td id="age_${p.id}">${p.age}</td>
		</tr>
		`
	).join('');
};
const removePerson = async (id = -1) => {
	const res = await fetch(`./api/people/${id}`, {method: 'DELETE'})
		.then(j => j.json())
		.catch(e => console.err(e))
		.then(j => console.log(j));
	if(!res)
		people();
};
const addPerson = async () => {
	const p = {
		'firstname': document.querySelector('#firstname_0').value.trim(),
		'lastname': document.querySelector('#lastname_0').value.trim(),
		'age': parseInt(document.querySelector('#age_0').value.trim())
	};
	if(
		p.firstname !== '' && p.lastname !== '' &&
		p.age !== NaN && p.age > -1
	) {
		await fetch(
			'./api/people', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify(p)
			})
			.then(j => j.json())
			.catch(e => console.error(e));
		people();	// ricarica la pagina
	}
	else {
		alert('Non hai inserito nulla!');
	}
}