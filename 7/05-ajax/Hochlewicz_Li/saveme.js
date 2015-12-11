var ij = document.getElementById('injones');
var qs = document.getElementById('quicksand');
var dn = document.getElementById('drowning');
            
function init(){
	qs.style.position = 'absolute';
	qs.style.top = '500px';
	qs.style.height = '500px';
    ij.style.position = 'relative'; 
    ij.style.left = '500px'; 
	ij.style.top = '0px'; 
	ij.style.height = '200px'; 
	ij.style.width = '118px'; 
	ij.style.zIndex = '1';
	dn.style.visibility = 'hidden';
	dn.style.position = 'relative';
	dn.style.left = '500px';
};
            
function drown(){
    ij.style.top = parseInt(ij.style.top) + 10 + 'px';
	checkifdrowning();
};
         
function jump(){
    ij.style.top = parseInt(ij.style.top) - 10 + 'px';
};

function checkifdrowning(){
	if (parseInt(ij.style.top) + parseInt(ij.style.height) > parseInt(qs.style.top)){
		dn.style.top = parseInt(ij.style.top) - 70 + 'px';
		dn.style.visibility = 'visible';
		checkifdead();
		changehelptext();
	}
	else{
		dn.style.visibility = 'hidden';
	}
};

function checkifdead(){
	if (parseInt(ij.style.top) > 500){
		console.log('I am dead.');
		loadDoc()
	}
};

function changehelptext(){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (xhttp.readyState == 4 && xhttp.status == 200) {
			document.getElementById("helptext").innerHTML = xhttp.responseText;
		}
	};
  xhttp.open("GET", "almost_dead.txt", true);
  xhttp.send();
}
		 
function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
      document.getElementById("main").innerHTML = xhttp.responseText;
    }
  };
  xhttp.open("GET", "you_lose.txt", true);
  xhttp.send();
}		 
		 
window.onload = init;
myInterval = setInterval(drown,200);