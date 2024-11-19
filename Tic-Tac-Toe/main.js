let step, gameComplete;
let X = 0, O = 0;

// All the cells are stored in a NodeList
const boxes = document.querySelectorAll('.box');

// Start the game
function startGame() {
  step = 1;
  gameComplete = false; // To check if game has ended or not
  document.getElementById('button').innerHTML = '<h3>Reset!</h3>';
  document.getElementById('turn').innerHTML = `<h3>It's Player <img class="button-img" src="./1-16405_american-red-cross-computer-icons-christian-cross-symbol.png"> turn</h3>`;
  
  // Initialize pos array
  pos = ['', '', '', '', '', '', '', '', '']; // Changed to empty strings initially for reset
  
  // Clear the grid and set up event listeners
  boxes.forEach((box) => {
    box.innerHTML = '';
    box.classList.remove('winning'); // Remove previous highlights
    box.addEventListener('click', handler, { once: true });
  });
}

// Handler for each box click (cross or nought)
function handler(event) {
  if (step % 2 !== 0) {
    event.target.innerHTML = '<img class="cross" src="./1-16405_american-red-cross-computer-icons-christian-cross-symbol.png">';
    document.getElementById('turn').innerHTML = `<h3>It's Player <img class="button-img" src="./421-4211837_fond-colors-circle-poster-u37711-transparent-red-strikethrough.png"> turn</h3>`;
    pos[event.target.id] = 'x';
    winner('cross');
  } else {
    event.target.innerHTML = '<img class="nought" src="./421-4211837_fond-colors-circle-poster-u37711-transparent-red-strikethrough.png">';
    document.getElementById('turn').innerHTML = `<h3>It's Player <img class="button-img" src="./1-16405_american-red-cross-computer-icons-christian-cross-symbol.png"> turn</h3>`;
    pos[event.target.id] = 'o';
    winner('no');
  }
  step++;
}

// Function to determine the winner and highlight the winning boxes
function winner(val) {
  // Define all winning combinations (indices of boxes)
  const winningPatterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
    [0, 4, 8], [2, 4, 6] // Diagonals
  ];
  
  for (const pattern of winningPatterns) {
    if (pos[pattern[0]] === pos[pattern[1]] && pos[pattern[1]] === pos[pattern[2]] && pos[pattern[0]] !== '') {
      highlightWinningBoxes(pattern); // Highlight the winning boxes
      if (val === 'cross') {
        document.getElementById('turn').innerHTML = `<h3>&nbsp&nbsp<img class="button-img" src="./1-16405_american-red-cross-computer-icons-christian-cross-symbol.png"> Wins! Play Again</h3>`;
        X++;
        document.getElementById('scoreX').innerHTML = `<h4>${X}</h4>`;
      } else {
        document.getElementById('turn').innerHTML = `<h3>&nbsp&nbsp<img class="button-img" src="./421-4211837_fond-colors-circle-poster-u37711-transparent-red-strikethrough.png"> Wins! Play Again</h3>`;
        O++;
        document.getElementById('scoreO').innerHTML = `<h4>${O}</h4>`;
      }
      gameComplete = true;
      for (let i = 0; i < boxes.length; i++) {
        boxes[i].removeEventListener('click', handler); // Disable further clicks
      }
      return;
    }
  }

  // Check for draw (game is over)
  if (step === 9) { // Step 9 means all boxes are filled, and it's a draw if no winner
    document.getElementById('turn').innerHTML = "<h3>It's a DRAW! Play Again</h3>";
    gameComplete = true;
    for (let i = 0; i < boxes.length; i++) {
      boxes[i].removeEventListener('click', handler); // Disable further clicks in case of draw
    }
  }
}

// Function to highlight the winning boxes
function highlightWinningBoxes(pattern) {
  pattern.forEach(index => {
    const box = document.getElementById(index);
    box.classList.add('winning'); // Add the 'winning' class to highlight the box
  });
}

// Reset the game when 'Reset' button is clicked
document.getElementById('button').onclick = () => {
  reset();
};

// Reset function for a new game
function reset() {
  X = 0;
  O = 0;
  document.getElementById('scoreO').innerHTML = `<h4>${O}</h4>`;
  document.getElementById('scoreX').innerHTML = `<h4>${X}</h4>`;
  startGame();
}

// Reset highlights when starting a new game
function removeWinningHighlights() {
  boxes.forEach((box) => {
    box.classList.remove('winning'); // Remove the 'winning' class from all boxes
  });
}

// Start the game for the first time
startGame();

// Continue the game when the turn display is clicked
document.getElementById('turn').onclick = () => {
  if (gameComplete) {
    startGame();
  }
};
