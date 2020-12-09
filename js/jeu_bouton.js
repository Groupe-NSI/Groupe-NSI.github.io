var nombre = 0

function commencer() {
	document.getElementById('start').style.display = "none";
  document.getElementById('jouer').style.display = "block";
  
  nombre = Math.floor(Math.random() * Math.floor(200));
}

function deviner() {
	var valeur = document.getElementById('entree').value;
  if (valeur > nombre) {
  	alert("Plus bas!")
  } else if (valeur < nombre) {
  	alert("Plus haut!")
  } else {
  	alert("Tu as un qi de " + nombre)
  }
}
