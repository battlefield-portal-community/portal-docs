---
title: Set Custom Time and Target Score
date: 2023-10-12T13:52:22+05:30
draft: false
geekdocAnchor: true
weight: 3
---

When setting the time and target score, there are 2 ways to acheive this depending if you are using a CORE game mode or a CUSTOM game mode.

{{< toc >}}

## CORE

If you are using any of the CORE game modes then you can do this using the modifiers.

Go to:

- CORE - Game Mode Details

From here you can alter the Game Time and the Reinforcement Multiplier.

![modifier](images/modifier.PNG)

---

## CUSTOM

When using a CUSTOM game mode you will need to use the editor.

We can do this using 2 blocks:

- SetGameModeTImeLimit
- SetGameModeTargetScore

Please Note:
All game modes apart from Conquest count up to their target score.
Conquest will always count DOWN. So if the score is less than the target, the game mode will end. For Conquest you will want to use the SetGameModeScore block for each team.

![test](images/score.PNG)
