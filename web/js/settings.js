function setData(elem) {
	localStorage[elem.getAttribute('name')] = JSON.stringify([elem.getAttribute('id'), elem.getAttribute('value')]);
}

function setChecked() {
	let elem = JSON.parse(localStorage.getItem('tempRadios'))[0];
	document.getElementById(elem).checked = true;
}

setChecked();
