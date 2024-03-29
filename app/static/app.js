var numSelected = null;
var puzzle;

window.onload = function(){
    setGame();
    setDigits();
	startTimer();
}

// Part A: Initial and Refresh the game //

function setGame() {
    puzzle = new generateSudoku();
	for(var i = 0; i < 9; i++) {
		for(var j = 0; j < 9; j++) {
			var tile = document.getElementById("t" + i + "x" + j);
			if(puzzle.getTileNumber(i, j) === 0) {
				tile.className = "emptyCell";
				tile.innerHTML = "";
				tile.onclick = selectTile;
			}
			else {
					tile.style.backgroundColor = "#ecf4f3";
					tile.className = "cell";
					tile.innerHTML = puzzle.getTileNumber(i, j);
			}
		}
	}
	
	reset();
}

function setDigits() {
    // set digits
    for (let i = 1; i <= 9; i++) {
        let number = document.createElement("div");
        number.id = i;
        number.innerHTML = i;
        number.addEventListener("click", selectNumber)
		// When click on the number, the number is selected.
        number.classList.add("number");
        document.getElementById("digits").appendChild(number); // display the digit box
    }
}


function newGame() {
	// generate a new grid with random sudoku
	location.reload();
}

// Part B: Generate Sudoku//

function generateSudoku() {
    
    // a random complete sudoko example 
	var grid = [
        [5, 8, 1, 6, 7, 2, 4, 3, 9],
        [7, 9, 2, 8, 4, 3, 6, 5, 1],
        [3, 6, 4, 5, 9, 1, 7, 8, 2],
        [4, 3, 8, 9, 5, 7, 2, 1, 6],
        [2, 5, 6, 1, 8, 4, 9, 7, 3],
        [1, 7, 9, 3, 2, 6, 8, 4, 5],
        [8, 4, 5, 2, 1, 9, 3, 6, 7],
        [9, 1, 3, 7, 6, 8, 5, 2, 4],
        [6, 2, 7, 4, 3, 5, 1, 9, 8]
    ];

    // the tile matrix
	var hiddenGrid = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0, 0, 0]
		];

	shuffle(grid); //randomly shuffle the lists in grid
	hideTiles(grid, hiddenGrid);

	this.getTileNumber = function(row, col) {
		return hiddenGrid[row][col];
	};

	this.getSolution = function(row, col) {
		return grid[row][col];
	};	

	// This is a solution checking
	this.isValidSudoku = function(finishedGrid) {
		var map = [];
		var tmp = 0;
		for (var i = 0; i < 9; i++) {
		  for (var j = 0; j < 9; j++) {
			tmp = finishedGrid[i][j];
			if (tmp === '') continue;
			if (map['i' + i + tmp] || map['j' + j + tmp] || map['b' + Math.floor(i / 3) + Math.floor(j / 3) + tmp]) return false;
			map['i' + i + tmp] = 1;
			map['j' + j + tmp] = 1;
			map['b' + Math.floor(i / 3) + Math.floor(j / 3) + tmp] = 1;
		  }
		}
		return true;
	};
}




function shuffle(grid) {
	// Way to update new puzzle

	var i, j, temp,  col1, col2, row1, row2, sub;

	//swap all columns within each subsquare
	for(i = 0; i < 25; i++) {
		sub = Math.floor(Math.random()*3);
		col1 = Math.floor(Math.random()*3);
		col2 = Math.floor(Math.random()*3);
		while(col1 == col2) col2 = Math.floor(Math.random()*3);
		for(j = 0; j < grid.length; j++) {
			temp = grid[j][sub*3 + col1];
			grid[j][sub*3 + col1] = grid[j][sub*3 + col2];
			grid[j][sub*3 + col2] = temp;
		}
	}  
	

	//swap all rows within each subsquare
	for(i = 0; i < 25; i++) {
		sub = Math.floor(Math.random()*3);
		row1 = Math.floor(Math.random()*3);
		row2 = Math.floor(Math.random()*3);
		while(row1 == row2) row2 = Math.floor(Math.random()*3);
		for(j = 0; j < grid.length; j++) {
			temp = grid[sub*3 + row1][j];
			grid[sub*3 + row1][j] = grid[sub*3 + row2][j];
			grid[sub*3 + row2][j] = temp;
		}
	}  

}

function hideTiles(aGrid, hiddenGrid) {

	// Randomly hide tiles, no guarantee for a unique solution
	var numTiles, k;

	for(var i = 0; i < 9; i++) {
		for(var j = 0; j < 9; j++) {
			hiddenGrid[i][j] = aGrid[i][j];
		}
	}

	for(var i = 0; i < 4; i++) {
		numTiles = Math.floor(Math.random()*8 + 6);
		while(numTiles > 0) {
			k = Math.floor(Math.random()*9);
			hiddenGrid[i][k] = 0;
			hiddenGrid[8-i][8-k] = 0;
			numTiles--;
			
		}
	}

	numTiles = Math.floor(Math.random()*4 + 2);
	while(numTiles > 0) {
		k = Math.floor(Math.random()*4);
		hiddenGrid[4][k] = 0;
		hiddenGrid[4][8-k] = 0;
		numTiles--;
	}
}


// Part C: Play the game (number board setting and erase functions) //

function selectNumber() {
    if (numSelected != null) {
        numSelected.classList.remove("number-selected");
    }
    numSelected = this;
    numSelected.classList.add("number-selected");
}


function selectTile() {
    if (numSelected) {
        this.innerText = numSelected.id;
    } // New selected number can replace the existed one
	if (numSelected == null) {
        this.innerText = "";
    }
}

function erase(){
	// remove any number from the selected tile
	numSelected = null;
}


// Part D: Solution checking //

function check() {
	if (checkForEmptyCells() === true){ 
		var finishedGrid = finishGrid();
			if (puzzle.isValidSudoku(finishedGrid)){
					pause();
					document.getElementById('result').innerHTML = "You did amazing!!" + " The time you spent is " + timeSpent + " seconds";
					return timeSpent;
			} else {
					document.getElementById('result').innerHTML = "Something needs to be revised :(";
					startTimer();
					return false;
			}
	} else {
		// user cannot submit an incomplete sudoku
		document.getElementById('result').innerHTML = "Please finish the sudoku";
		startTimer();
		return false;
	}
}

function submit() { 
	if (check() != false) {
		$.ajax({
			url: "/home", 
			type: "POST",  
			data: {
				 "timeSpent": timeSpent},  
		});
		console.log(timeSpent);
	} else if (checkForEmptyCells() === false) {
		document.getElementById('result').innerHTML = "Please finish the sudoku";
		startTimer();
	} else {
		document.getElementById('result').innerHTML = "Something needs to be revised :(";
		startTimer();
	}
}

function finishGrid() {
	// record the finished grid(the current puzzle)
	var finishedGrid = new Array(9);
	for(var i = 0; i < 9; i++) {
		finishedGrid[i] = new Array(9);
		for(var j = 0; j < 9; j++) {
			finishedGrid[i][j] = document.getElementById("t" + i + "x" + j).innerHTML;
		}
	}
	return finishedGrid;
}


function solve() {
	for(var i = 0; i < 9; i++) {
		for(var j = 0; j < 9; j++) {
			var tile = document.getElementById("t" + i + "x" + j);
			tile.innerHTML = puzzle.getSolution(i, j);	
		}
	}
} 


function checkForEmptyCells() {
	// check for the completeness of the current puzzle
	for(var i = 0; i < 9; i++) {
		for(var j = 0; j < 9; j++) {
			var tile = document.getElementById("t" + i + "x" + j);
			if(tile.innerHTML == "") return false;
		}
	}
	return true;
}

// Part E: Timer //
var timeSpent = 0;
let myTimer = null;

function timer() {
	// A function that would continuously growing per second
    timeSpent += 1;
	var hour = 0;
	var min = parseInt(timeSpent/60); // minutes
	var sec = timeSpent % 60; // seconds 
	if (sec < 10) {
		var s = '0' + sec;
	} else { var s = sec;}
	if (min < 10) {
		var m = '0' + min; 
		var h = '00';
	} else if(min >=60) {
		hour++;
		min = 0;
	} else {
		var m = min;
	}
	if (hour == 0) {
		document.getElementById('showNum').innerHTML = m + ':' + s;
	} else if (hour < 10) {
		var h = '0' + hour;
		document.getElementById("showNum").innerHTML = h + ':' + m + ':' + s;
	} else {
		var h = hour.toString();
		document.getElementById("showNum").innerHTML = h + ':' + m + ':' + s;
	} 
    
}

function startTimer(){
	// the start button
	// The puzzle will be shown when timer starts
	document.getElementById('grid').style.visibility = "visible";

    if(myTimer == null){
        myTimer = setInterval(timer,1000); 
    }
	if (document.getElementById('pause').style.display = "none"){
		document.getElementById('pause').style.display = "block";
	} 
	if (document.getElementById('start').style.display = "block"){
		document.getElementById('start').style.display = "none";
	}
	
}

function pause(){
	// the pause button
    clearInterval(myTimer);
    myTimer = null;
	document.getElementById('start').style.display = "block";
	document.getElementById('pause').style.display = "none";
}

function reset(){ 
	// reset time 
	document.getElementById("showNum").innerHTML = '00' +':'+ '00';
    timeSpent = 0;
}

// Part F: Share //

function clip_text(a_string){
    var input = document.createElement('input')
    input.id="__copyText__";
    input.value = document.getElementById(divId).innerText;
    document.body.appendChild(input);
    input.select();
    document.execCommand("copy");
    var txt = input.value
    input.remove()
    console.log("OK COPIED: '"+txt+"'")
}
function clip_div(divId){
   return clip_text(document.getElementById(divId).innerText)
}

// We tried to create a mechanism that we can copy the result and past it to the clipboard, then share the result on other social media.