document.getElementById('nomalea').onclick = function() {
	if (this.checked) {
  	document.getElementById('nom').style.display ="none";
  } else {
  	document.getElementById('nom').style.display ="block";
  }
}

document.getElementById('prenomalea').onclick = function() {
	if (this.checked) {
  	document.getElementById('prenom').style.display ="none";
  } else {
  	document.getElementById('prenom').style.display ="block";
  }
}

document.getElementById('agealea').onclick = function() {
	if (this.checked) {
  	document.getElementById('age').style.display ="none";
  } else {
  	document.getElementById('age').style.display ="block";
  }
}

document.getElementById('delialea').onclick = function() {
	if (this.checked) {
  	document.getElementById('deli').style.display ="none";
  } else {
  	document.getElementById('deli').style.display ="block";
  }
}
