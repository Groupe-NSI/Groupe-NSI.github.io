var nombre = 0

document.getElementById('commencer').onclick = function() {
	document.getElementById('start').style.display = "none";
  document.getElementById('jouer').style.display = "block";
  
  nombre = Math.floor(Math.random() * Math.floor(200));
}

document.getElementById('valider').onclick = function() {
	var valeur = document.getElementById('entree').value;
  if (valeur > nombre) {
  	alert("Plus bas!")
  } else if (valeur < nombre) {
  	alert("Plus haut!")
  } else {
  	alert("BRAVO BG!")
  }
}
