var numSelected = null;
var tileSelected = null;


window.onload = function(){
    setGame();
    setDigits();
	startTimer();
}

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
    // set board
    /*for (let row = 0; row < 9; row++) {
        for (let col = 0; col < 9; col++) {
            let tile = document.createElement("div");
            tile.id = row.toString() + "." + col.toString();
            tile.addEventListener("click", selectTile)
            tile.classList.add("tile");
            document.getElementById("board").append(tile);
        }
    } */
}
function setDigits() {
    // set digits
    for (let i = 1; i <= 9; i++) {
        let number = document.createElement("div");
        number.id = i;
        number.innerHTML = i;
        number.addEventListener("click", selectNumber)
        number.classList.add("number");
        document.getElementById("digits").appendChild(number);
    }
}


// Revision
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
	var hGrid = [
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

	shuffle(grid); //randommly shuffle the lists in grid
	hideTiles(grid, hGrid);

	this.getTileNumber = function(row, col) {
		return hGrid[row][col];
	};

	this.getSolution = function(row, col) {
		return grid[row][col];
	};

	this.isValid = function(fGrid, row, col, val) {
		var rowCnt = this.countInstances(fGrid[row], val);
		var colCnt = this.countInstances(this.columnToArray(fGrid, col), val);
		var subCnt = this.countInstances(this.subsquareToArray(fGrid, row, col), val);
		if(rowCnt == 1 && colCnt == 1 && subCnt == 1) {
			return true;
		}
		return false;
	};

	this.columnToArray = function(fGrid, col) {
		var colArray = [];
		for(var i = 0; i < 9; i++) {
			colArray.push(fGrid[i][col]);
		}
		return colArray;
	};

	this.subsquareToArray = function(fGrid, row, col) {
		var subArray = [];
		var subrow = row - (row % 3);
		var subcol = col - (col % 3);
		for(var i = 0; i < 3; i++) {
			for(var j = 0; j < 3; j++) {
				subArray.push(fGrid[i+subrow][j+subcol]);
			}
		}
		return subArray;
	};

	this.countInstances = function(arr, val) {
		var cnt = 0;
		for(var i = 0; i < arr.length; i++) {
			if(arr[i] == val) cnt++;
		}
		return cnt;
	};
}

function shuffle(grid) {

	var i, j, k, temp, col, col1, col2,
	row1, row2, sub, sub1, sub2, num1, num2;

	//swap the same columns of each subsquare
	for(i = 0; i < 25; i++) {
		col = Math.floor(Math.random()*3);
		sub1 = Math.floor(Math.random()*3);
		sub2 = Math.floor(Math.random()*3);
		for(j = 0; j < grid.length; j++) {
			temp = grid[j][col + sub1*3];
			grid[j][col + sub1*3] = grid[j][col + sub2*3];
			grid[j][col + sub2*3] = temp;
		}
	}

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

	//swap one number with another
	for(i = 0; i < 25; i++) {
		num1 = Math.floor(Math.random()*9 + 1);
		num2 = Math.floor(Math.random()*9 + 1);
		while(num1 == num2) num2 = Math.floor(Math.random()*9 + 1);
		for(j = 0; j < grid.length; j++) {
			for(k = 0; k < grid[j].length; k++) {
				if(grid[j][k] == num1)
					grid[j][k] = num2;
				else if(grid[j][k] == num2)
					grid[j][k] = num1;
			}
		}
	}
}

function hideTiles(aGrid, hiddenGrid) {

	// Randomly hide tiles, no guarantee for a unique solution
	var numTiles, k;

	for(var c = 0; c < 9; c++) {
		for(var d = 0; d < 9; d++) {
			hiddenGrid[c][d] = aGrid[c][d];
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

// Revision end



function selectNumber() {
    if (numSelected != null) {
        numSelected.classList.remove("number-selected");
    }
    numSelected = this;
    numSelected.classList.add("number-selected");
}


// we do not need selecttile function?
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

function redo(){
 
}

// Erase button
function erase(){
    for (let i = 1; i <= 9; i++) {
        let clear = null;
        document.getElementById("digits").appendChild(null);
    }
}

// Timer

let int =null;
let num = 0;

// A function that would continuously growing per second

function timer() {
    num += 1;
	var hour = min/60; // hours needs revision
    var min = parseInt(num/60); // minutes
    var sec = num % 60; // seconds
    document.getElementById("showNum").innerHTML = hour + ':' + min + ':' + sec;
}

// the start button
function startTimer(){
    if(int == null){
        int = setInterval(timer,1000); 
    }
	if (document.getElementById('pause').style.display = "none"){
		document.getElementById('pause').style.display = "block";
	} 
	if (document.getElementById('start').style.display = "block"){
		document.getElementById('start').style.display = "none";
	}
	
}

// the pause button
function pause(){
    clearInterval(int);
    int = null;
	document.getElementById('start').style.display = "block";
	document.getElementById('pause').style.display = "none";
}


// reset button
function reset(){
    if (int == null) {
        num = 0;
        document.getElementById("showNum").innerHTML = num +':'+num;
    }
}

