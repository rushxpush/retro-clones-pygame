## Todo

### ⬛ Core Gameplay
- ✅ Implement game loop
- ✅ Handle player paddle movement
- ⬛ Improve paddle control: store and use last pressed key
- ✅ Create Ball class with movement
- ✅ Handle ball-wall collision

### ⬛ Gameplay Features
- ✅ Implement field visuals (center divider and boundary lines)
- ✅ Add enemy paddle (Player 2)
- ⬛ Add AI to player 2 paddle 
- ⬛ Implement scoring system
- ⬛ Display score using text rendering

### ⬛ UI and Game States
- ✅Refactor code to run inside a game screen/state system
- ✅ Implement Main Menu screen
- ✅ Create basic UI components (buttons, labels)
- ⬛ Implement Pre-Game Config screen (target score, difficulty)
- ⬛ Implement Game Over screen (winner display, restart option)

### ⬛ Visual and UX Polish
- ⬛ Improve text renderer for UI screens

### ⬛ Gameplay improvement
- ⬛ Reduce paddle collision box 

### Bugs
- ⬛ Pressing the key up against the wall makes the paddle render inside de wall

## Dev Notes (for future blog)

### Why I Started Classic Games Clone Series
I want to deeply understand game development, starting from simple projects and progressively increasing complexity. I tried and failed many times to create my "dream game" of the moment, and I always got stuck trying to tackle too much complexity at the same time. 

This time I decided to study "correctly" and learn by clone classic games like Pong, Space Invaders, Tetris, and so on. Every game I choose increases the difficulty little by little and I feel like this solves the problem of being overwhelmed by too much complexity at the same time. 

For example, one time I decided to create a 3D shooter with javascript and three.js. I got stuck trying to learn game mechanics, trying to correctly render stuff on the stuff, dealing with collision bugs, trying to decide the game architeture and so on, all at the same time. This made the development a slog and a mess. 

Cloning classic games like Pong, Tetris, and platformers allows me to learn core mechanics without getting stuck on game design decisions. The next time I'll try to tackle a complex genre like a FPS, I'll already have practiced important stuff used in this genre like AI, collision, how to create menus, UIs, etc

### Design Decisions
- Using Python and Pygame for simplicity and speed of iteration. 
- Structuring the project using a "game states" architecture (Menu, Gameplay, Game Over, etc).
- Decided to use Rect-based collision for simplicity in Pong.

### Lessons Learned So Far
- Handling keyboard input in games is more subtle than I expected. For example, deciding whether to track key states vs. last key pressed. This is the kind of stuff that we take for granted when playing a game, but makes all the difference on the experience.
- Separating game objects (Paddle, Ball) from game state logic made the code easier to manage. I already got web dev experience with this, so it made sense to make the game objects separated. Maybe the code is a bit over engineered for a PONG clone, but I'm thinking about some future modifications I'd like to do to the gameplay. And more important, I want to reuse what's possible from the PONG clone code on the next projects, maybe creating a library of reusable components.
- Even the simplest game can be a challenge to code and make smooth. There's always something to be done and the temptation to 'scope creep' is ever present.

### Next Technical Challenges
- Implementing a flexible state management system for screens.
- Creating a reusable UI system (starting with buttons and text).
- Handling AI or 2-player input for the second paddle.
- Create a StateManager to manager the screen transitions


✅ Outros tópicos  ir anotando conforme progride:
Other topics to jot down while I'm making progress on the game:

- Difficulties found during development
- Important architectural decisions
- Mistakes I made and how I solved then
- Small interesting bugs that happened
- Ideas of stuff that could be better that I'll just put on the backlog
- Reflexios about my learning (ex.: "never thought a PONG clone would teach me something like this or that...")