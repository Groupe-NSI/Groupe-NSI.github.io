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
	document.body.style.backgroundImage = "url('https://file1.telestar.fr/var/telestar/storage/images/3/1/5/0/3150739/vincent-lagaf-dans-strike.jpg?alias=original')"
  } else if (valeur < nombre) {
  	alert("Plus haut!")
	document.body.style.backgroundImage = "url('https://www.premiere.fr/sites/default/files/styles/scale_crop_1280x720/public/2018-04/Audiences-TV-Le-juste-prix-de-Vincent-Lagaf-atteint-des-sommets.jpg')"
  } else {
  	alert("Tu as un qi de " + nombre)
	document.body.style.backgroundImage = "url('https://cdn.discordapp.com/attachments/785944479853051954/786286026606903326/telechargement.jpeg')"
  }
}
