'use strict';
const fields = ['firstname', 'lastname', 'age'];

// reload data and write on your page the data from remote server
const people = async _ => {
	document.querySelector('#buddylist').innerHTML = (await personList()).map( p =>
		`
		<tr>
		<td id="firstname_${p.id}">${p.firstname}</td>
		<td id="lastname_${p.id}">${p.lastname}</td>
		<td id="age_${p.id}">${p.age}</td>
		<td id="toggle_${p.id}" class="toggle_on" onclick="editPerson(${p.id})"></td>
		<td id="abort_${p.id}" class="delete" onclick="removePerson(${p.id})"></td>
		</tr>
		`
	).join('');
	erase();
}

// edit mode
const editPerson = async (id) => {
	let p2edit = {};
	for(let field of fields) {
		p2edit[field] = document.querySelector(`#${field}_${id}`).innerHTML;
		document.querySelector(`#${field}_${id}`).innerHTML = `
		<input
			id="edit_${field}_${id}"
			class="form-control" 
			type="${field==='age'? 'number':'text'}"
			value="${p2edit[field]}"/>
		`;
	}
	let toggle_btn = document.querySelector(`#toggle_${id}`);
	let abort_btn = document.querySelector(`#abort_${id}`);
	toggle_btn.className = 'toggle_off';
	abort_btn.className = 'abort';
	toggle_btn.onclick = _ => {
		const person =  {
			'firstname': document.querySelector(`#edit_firstname_${id}`).value,
			'lastname': document.querySelector(`#edit_lastname_${id}`).value,
			'age': parseInt(document.querySelector(`#edit_age_${id}`).value)
		}
		console.log(JSON.parse( JSON.stringify(person)));
		modifyPerson(id, person);
	}
	abort_btn.onclick = _ => people();
};

// form clear
const erase = async _ => fields.map(leaf => document.querySelector(`#${leaf}_0`).value= '');

// CREATE
const addPerson = async _ => {
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
const personList = async _ => await fetch('./api/people')
	.then(res => res.json())
	.catch(e => console.err(e))
	.then(j => j.length === 0 ? [] : j.sort((p1, p2) => (p1.lastname > p2.lastname) ? 1 : -1));

// UPDATE
const modifyPerson = async (id = -1, p = {}) => {
	const res = await fetch(`./api/people/${id}`, {
		method: 'PUT',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(p)
	})
		.then(j => j.json())
		.catch(e => console.err(e))
		.then(j => console.log(j));
	if(!res)
		people();
};
/*
Sorry but something was wrong.
Maybe later on you could find the right code.
But now not yet!

If you want an early right code, try to move your fingers on keyboard and fell craziness in your head!
This is a good way to develop a nice code or become a crazy programmer!

Good Luck, Programmer!

You must be a good programmer and you must be proud of your mistakes
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