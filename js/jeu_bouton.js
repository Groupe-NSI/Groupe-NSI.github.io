var nombre = 0

function commencer() {
	document.getElementById('start').style.display = "none";
  document.getElementById('jouer').style.display = "block";
  
  nombre = Math.floor(Math.random() * Math.floor(200));
}

function deviner() {
	var valeur = document.getElementById('entree').value;
  if (valeur > nombre) {
	document.body.style.backgroundImage = "url('https://groupe-nsi.github.io/img/plus_bas.jpg')";
  	alert("Plus bas!");
  } else if (valeur < nombre) {
	document.body.style.backgroundImage = "url('https://groupe-nsi.github.io/img/plus_haut.jpg')";
  	alert("Plus haut!");
  } else {
	document.body.style.backgroundImage = "url('https://groupe-nsi.github.io/img/gagne.jpg')";
  	alert("Tu as un qi de " + nombre);
  }
}
