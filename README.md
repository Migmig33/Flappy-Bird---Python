### PyGame Flappy Bird Clone V1

A fully functional 2D side-scrolling game built with python and PyGame, inspired by the classic game mobile hit Flappy Bird. This project demonstrates core game development concepts including physics simulation and collision detection.

## 🚀 Features
- Dynamic Physics: Implements gravity and jumps mechanics for player-controlled bird
- Scoring System: Tracks and display score if the bird passed through the pipes
- Restart Mechanic: A custom-built UI button class the allows player to reset the game without restarting the program
- Procedural Obstacles: Randomly generated pipes that scroll across the screen at varying heights.

## 🎮 Controls
- Left Mouse Click: Make the bird fly/jump
- Restart Button: Reset the game if the game is over


## 🛠️ Technologies Used
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyGame](https://img.shields.io/badge/PyGame-00A86B?style=for-the-badge&logo=python&logoColor=white)

## 📂 Project Structure
```

FlappyBird/
├── assets/ 
|    ├──images/          # Images Folder (bird.png, pipe.png, background.png)
|    └──sounds/          # Sounds Folder (bgm.mp3, score.mp3, game_over.mp3)       
|           
├── game/                # Class Folder
│    ├──__init__.py    
│    ├──bird.py          # Bird Class
│    ├──pipe.py          # Pipe Class
|    └──button.py        # Button Class
|
├── main.py              # Main File
├── config.py            # Configuration of the Game
└── README.md            # Project documentation

```
## 🚀 Installation 

### 1. Clonse Repository
```bash
git clone https://github.com/Migmig33/Flappy-Bird---Python.git
cd project-name
```

### 2. Install Library
    - Open Project Terminal
    - Enter `pip install pygame`

### 3. Run the Game
    - Open Project Terminal
    - Enter `python main.py`

## Screenshot
**Main Menu**
<img width="726" height="947" alt="image" src="https://github.com/user-attachments/assets/61a1fc8c-9d0b-4146-9757-8e86f8a080a1" />


**Game Running**
<img width="728" height="947" alt="image" src="https://github.com/user-attachments/assets/0ea0bc00-c7b4-4cde-ab35-358c0648e155" />


**Game Over**
<img width="727" height="946" alt="image" src="https://github.com/user-attachments/assets/387ed289-5a08-498b-a067-39da46a56de5" />
