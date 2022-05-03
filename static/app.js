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

// the start button
document.getElementById("start").addEventListener('click',function(){
    if(int == null){
        int = setInterval(startNum,1000);
    }
})

document.getElementById("pause").addEventListener('click', function () {
    clearInterval(int);
    int = null;
});

// reset button
 let num = 0;
 function start(){
    document.getElementById("display").innerHTML = 1;
 }

 if(int == null){
    int = setInterval(startNum,1000);
}
 document.getElementById("reset").addEventListener('click', function () {
     if (int == null) {
         num = 0;
         document.getElementById("showNum").innerHTML = num;
     }
 });

 function startNum() {
     num++;
     document.getElementById("showNum").innerHTML = num;
 }
