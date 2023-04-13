'use strict';
// reload data and write on your page the data from remote server
const people = async () =>
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

// CREATE
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
		people();	// reload your page and update your data
	}
	else {
		alert('Something is wrong!');
	}
};

// READ
const personList = async () => await fetch('./api/people')
	.then(res => res.json())
	.catch(e => console.err(e))
	.then(j => j.length === 0 ? [] : j.sort((p1, p2) => (p1.lastname > p2.lastname) ? 1 : -1));

// UPDATE
/*
Sorry but something was wrong.
Maybe later you could find a right code.
Now not yet!

If you want an early right code, try to move your finghers on keybord and fell craziness will begen in your head!
This is a good way to develop a nice code or begen a crazy programmer!

Good Luck, Programmer!

You must a good programmer and you must proud of your wrongs
*/

// DELETE
const removePerson = async (id = -1) => {
	const res = await fetch(`./api/people/${id}`, {method: 'DELETE'})
		.then(j => j.json())
		.catch(e => console.err(e))
		.then(j => console.log(j));
	if(!res)
		people();
};
