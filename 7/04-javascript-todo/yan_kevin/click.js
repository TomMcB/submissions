var addToDo = function addToDo(s){
    var t = document.getElementById("to-do");
    var td = document.createElement("td");
    td.innerHTML = s;
    var tr = document.createElement("tr");
    tr.appendChild(td);
    t.appendChild(tr);
};

var removeToDo = function removeToDo(n){
    var tditems = document.getElementByTagName("td");
    tditems[n].remove();
    return tditems[n].innerHTML;
};

var bCallback = function bCallback(e){
    addToDo("HUE");
};

var b = document.getElementById("add");
b.addEventListener("click", bCallback);

var tdCallback = function tdCallback(e){
    addToDo("HUE");
};

var tododata = document.getElementByClassName('to-do-data');
tododata.addEventListener("mouseover", tdCallback);
