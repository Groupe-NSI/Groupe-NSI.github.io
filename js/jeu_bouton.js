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
	document.body.style.backgroundImage = "url('https://64.media.tumblr.com/4ee9b7af81c625b09c5693c8fef6a574/tumblr_inline_pk6hrjSWI31rkpscc_400.gifv')";
  	alert("Tu as un qi de " + nombre);
  }
}
