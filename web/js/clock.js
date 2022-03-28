async function currentTime(){
	const time = await eel.current_city_time()();
	let hour = time[0];
	let min = time[1];
	let sec = time[2];

	hour = updateTime(hour);
	min = updateTime(min);
	sec = updateTime(sec);

	document.getElementById("time").innerHTML = `${hour}:${min}:${sec}`;
	let timeout = setTimeout(function() { currentTime() }, 1000);
}

function updateTime(n) {
	if(n < 10) {
		return `0${n}`;
	} else {
		return n;
	}
}

currentTime();
