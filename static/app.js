var numSelected = null;
var tileSelected = null;


window.onload = function(){
    setGame();
}

function setGame() {
    // set digits
    for (let i = 1; i <= 9; i++) {
        let number = document.createElement("div");
        number.id = i;
        number.innerHTML = i;
        number.addEventListener("click", selectNumber)
        number.classList.add("number");
        document.getElementById("digits").appendChild(number);
    }
    // set board
    for (let row = 0; row < 9; row++) {
        for (let col = 0; col < 9; col++) {
            let tile = document.createElement("div");
            tile.id = row.toString() + "." + col.toString();
            tile.addEventListener("click", selectTile)
            tile.classList.add("tile");
            document.getElementById("board").append(tile);
        }
    }
}

function selectNumber() {
    if (numSelected != null) {
        numSelected.classList.remove("number-selected");
    }
    numSelected = this;
    numSelected.classList.add("number-selected");
}

function selectTile() {
    if (numSelected) {
        if (this.innerText != "") {
            return;
        }
        this.innerText = numSelected.id;
    }
}

// 4 functional buttons in Home page

// Undo button
function undo(){

}

// Erase button

// Notes button

// Hint button

// Timer

let int =null;
let num = 0;

// A function that would continuously growing per second

function timer() {
    num += 1;
    var min = parseInt(num/60); // minutes
    var sec = num % 60; // seconds
    document.getElementById("showNum").innerHTML = min + ':' + sec ;
}

// the start button
function start(){
    if(int == null){
        int = setInterval(timer,1000); 
    }
}

// the pause button
function pause(){
    clearInterval(int);
    int = null;
}


// reset button
function reset(){
    if (int == null) {
        num = 0;
        document.getElementById("showNum").innerHTML = num +':'+num;
    }
}

