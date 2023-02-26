<h1> Python Connect 4 game </h1>

A Connect 4 project in progress with local and online multiplayer\. Made with python and the pygame library\. The project is functional, the client can connect to the server, several games can be played at the same time\. 

**Purpose of this project :**
- Improving my knowledge of python
- Learn to create a network application
- Learn how to create a game 

**Requirements :** 
- python3 or higher
- pygame library

**Install pygame with python3 :** 
```
pip install pygame --pre
```

**This repository actually contains two softwares** : 
- The game client which contains the menus, assets, game interface and dialogue functions with the server\.
- The server which hosts the games, contains the logic for the networked games and manages multi-client connections\.

<h2> Client </h2>

The client contains classes and menus to play Power 4 locally or connect to the server to play online\. For the moment, there is no executable because the final release has not been done but it will be added soon\. 

**Launch the client with the command in ./client/src :**
```
py.exe .\run_game.py
```

<h3> Main menu </h3>

From this basic menu, you can play a local multiplayer game or an online multiplayer game\.

![main_menu](https://user-images.githubusercontent.com/63466144/221406479-068fd2fe-c98b-4df1-a32f-550fd13915b2.PNG)
