console.log("loaded script");

<!-- Make top 10 list -->
var ppg = document.getElementById("PPG");
var apg = document.getElementById("APG");
var rpg = document.getElementById("RPG");
var bpg = document.getElementById("BPG");
var output = document.getElementById("results");
var start = document.getElementById("cycle");	
var cyc = 0;
ppg.addEventListener("click", function(e) {
    $.get("/PPG", function(e) {
	output.innerHTML = e;
    });
    cyc = 1;
});

apg.addEventListener("click", function(e) {
    $.get("/APG", function(e) {
	output.innerHTML = e;
    });
    cyc = 2;
});

rpg.addEventListener("click", function(e) {
    $.get("/RPG", function(e) {
	output.innerHTML = e;
    });
    cyc = 3;
});

bpg.addEventListener("click", function(e) {
    $.get("/BPG", function(e) {
	output.innerHTML = e;
    });
    cyc = 4;
});

var pcounter = 0;
var acounter = 0;
var rcounter = 0;
var bcounter = 0;
var more = document.getElementById("advanced");
var list1 = ['James Harden', 'Kevin Durant', 'LeBron James', 'Anthony Davis', 'Carmelo Anthony', 'DeMarcus Cousins', 'Stephen Curry', 'LaMarcus Aldridge', 'Kobe Bryant', 'Blake Griffin'];
var list2 = ['Chris Paul', 'John Wall', 'Ty Lawson', 'Reggie Jackson', 'Ricky Rubio', 'Russell Westbrook', 'Rajon Rondo', 'Stephen Curry', 'Michael Carter-Williams', 'LeBron James'];
var list3 = ['Andre Drummond', 'DeMarcus Cousins', 'Pau Gasol', 'Tyson Chandler', 'Enes Kanter', 'Nikola Vucevic', 'Dwight Howard', 'Zach Randolph', 'LaMarcus Aldridge', 'Anthony Davis'];
var list4 = ['Hassan Whiteside', 'Serge Ibaka', 'Rudy Gobert', 'DeAndre Jordan', 'Tim Duncan', 'John Henson', 'Andre Drummond', 'Pau Gasol', 'Nerlens Noel', 'Terrence Jones'];

var cycle = function cycle() {
    if (cyc == 1) {
	$.get("/home/" + list1[pcounter], function(e) {
	    more.innerHTML = e;
	});
	pcounter++;
	if (pcounter == 10) {
	    pcounter = 0;
	}
    }
    if (cyc == 2) {
	$.get("/home/" + list2[acounter], function(e) {
	    more.innerHTML = e;
	});
	acounter++;
	if (acounter == 10) {
	    acounter = 0;
	}
    }
    if (cyc == 3) {
	$.get("/home/" + list3[rcounter], function(e) {
	    more.innerHTML = e;
	});
	rcounter++;
	if (rcounter == 10) {
	    rcounter = 0;
	}
    }
    if (cyc == 4) {
	$.get("/home/" + list4[bcounter], function(e) {
	    more.innerHTML = e;
	});
	bcounter++;
	if (bcounter == 10) {
	    bcounter = 0;
	}
    }
};
setInterval(cycle,5000);
