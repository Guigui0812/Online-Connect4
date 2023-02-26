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

<h2> The game client </h2>

The client contains classes and menus to play Connect 4 locally or connect to the server to play online\. For the moment, there is no executable because the final release has not been done but it will be added soon\. 

**Launch the client with the command in ./client/src :**
```
py.exe .\run_game.py
```

<h3> Main menu </h3>

From this basic menu, you can play a local multiplayer game or an online multiplayer game\.

![main_menu](https://user-images.githubusercontent.com/63466144/221406479-068fd2fe-c98b-4df1-a32f-550fd13915b2.PNG)

Choosing the local game mode will take you directly to the game interface, while for the online game you will have to configure your network settings\.

<h3> Online settings menu </h3>

This menu allows you to configure the address, port and nickname that will be used to play online\. 

![settings_menu](https://user-images.githubusercontent.com/63466144/221407119-726a981c-aa1b-417c-9e41-f524c826cebf.PNG)

This menu includes a configuration file that saves your information locally so you don't have to repeat the configuration each time\. When you are finished, press play to start the online mode\.

<h3> Waiting screen </h3>

While waiting for a player ready to face you, a loading screen will be displayed with music to keep you waiting\.

![Attente_joueur](https://user-images.githubusercontent.com/63466144/221407158-4597e6dc-4e76-4f42-bf37-01ad6763922a.PNG)

When the player is found, the game can begin.\

<h3> Game Screen </h3>

The game screen allows you to interact with the game to conduct the game, whether online or locally\.

![game_screen](https://user-images.githubusercontent.com/63466144/221407232-958fc87b-0b4d-4e6f-b4cd-f2bdeb4f944a.PNG)

This screen allows you, when it is your turn, to place a piece in the grid\. The text at the top of the screen indicates whether it is your turn to play or not\. An animation allows the piece to fall from the top to the bottom of the grid like in the real Connect 4 game\.

The game is won when 4 pieces of the same color are aligned\. A victory screen is then displayed\.

![end_screen](https://user-images.githubusercontent.com/63466144/221407305-ee1c88ab-c16f-43e7-bd54-8f6860b1540c.PNG)

By pressing space, you can return to the main menu and start another game\.

<h2> The game server </h2>
