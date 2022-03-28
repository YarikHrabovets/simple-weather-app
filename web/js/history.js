function generateList(arr) {
	let obj = document.getElementById("list");
	if(arr.length == 0) {
		let div = document.createElement("div");
		div.className = "alert alert-warning text-center fs-5";
		div.innerHTML = "Ваш список пока пуст.";
		obj.append(div);
	} else {
		for(i=0; i<arr.length; i++) {
			let div = document.createElement("div");
			div.className = "d-flex mb-3";

			let btn = document.createElement("button");
			btn.innerHTML = `${arr[i][`city_${i}`][0]}  (${arr[i][`date_${i}`]})`;
			btn.className = "list-group-item list-group-item-action";
			btn.id = `${arr[i][`city_${i}`][1]}`;
			btn.style.background = "#606470";

			let del_btn = document.createElement("button");
			del_btn.innerHTML = "Удалить";
			del_btn.className = "btn btn-secondary";
			del_btn.id = i;

			btn.onclick = async function () {
				await eel.get_from_history(btn.id)();
				window.open("index.html", "_self");
			}

			del_btn.onclick = async function () {
				await eel._remove(Number(del_btn.id))();
				obj.insertBefore(div, obj.firstChild);
				obj.removeChild(obj.firstChild);
			}

			div.append(btn);
			div.append(del_btn);
			obj.append(div);
		}
	}
}


async function getJsonData() {
	const userHistory = Promise.resolve(eel._load()());
	userHistory.then(function(arr){
		generateList(arr);
	});
}

getJsonData();
