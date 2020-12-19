document.getElementById('valider').onclick = function() {
	var sexe = "Mr";
	var prenom = document.getElementById('prenom').value;
	var nom = document.getElementById('nom').value;
  var debut = document.getElementById('debut').value;
  var fin = document.getElementById('fin').value;
	var medecin = document.getElementById('medecin').value;
	var jours = document.getElementById('jours').value;

  document.getElementById('feuille').style.display = "none";
  document.getElementById('attestation').style.display = "block";
  
  var r_sexe = document.getElementById("r_sexe");
  var r_nom = document.getElementById('r_nom');
  var r_prenom = document.getElementById('r_prenom');
  var r_medecin = document.getElementById('r_medecin');
  var r_debut = document.getElementById('r_debut');
  var r_fin = document.getElementById('r_fin');
  var r_jours = document.getElementById("r_jours");
  
  r_sexe.innerHTML = sexe;
  r_nom.innerHTML = nom;
  r_prenom.innerHTML = prenom;
  r_medecin.innerHTML = medecin;
  r_debut.innerHTML = debut;
  r_fin.innerHTML = fin;
  r_jours.innerHTML = jours;
  
}
