---
title: Rules
date: 2023-10-12T13:52:22+05:30
draft: false

weight: 20
---

{{< toc >}}

# Fundamentals

## What is a game update-loop and tickrate?

Who could explain it best than an actual Battlefield Developer?
Darko Supe explains it in the following video very well and extensively.

**_If you want a short version continue reading down below._**

{{< youtube VzrSy1Z9cGs >}}

Almost every game uses a so-called **"Game/Update-Loop"** with a certain **"tickrate"**.
This loop contains several crucial actions that need to run frequently during a game.

For example these actions are (not accurate, but an abstraction):

- Getting the key input (which keys are you currently pressing)
- sending your activities and keystrokes to the server
- receiving other players activities from the server
- **Check if a determined event occurred and add it to the event queue**
- **Evaluate the gameplay rules against the current events in the queue**
- rendering the current game-state on your screen

The frequency by which this loop and its actions are running, is the so-called tickrate and is measured in hertz (actions/ticks per second).
Battlefield Portal servers have a tickrate of 40hz on PC and latest consoles. For old consoles the tickrate is only 20hz.

## Rules and Tickrate

When you open the Rules Editor you'll start with the grey "mod" block which holds all the rules you can specify.
This mod-block mimics the game-loop.
The rules you can specify in the mod-block are evaluated with every tick of the game.
This means they are checked/evaluated upt to 40 times per second - keep this in mind when coding your experience.
The rules are evaluated in sequential (one after another) order within the mod-block and not in parallel. This means that if you modify a value within the actions of one rule, the following rule already will have the modified values available.

# Rule-Block

**RULE** blocks are triggered from an in-game **EVENT**. When an **EVENT** triggers, the rule-block will check if its **CONDITION** has been met and then execute all of the **ACTIONS**.

## Rule Types

- **Ongoing**  
  Ongoing **RULE** types continually check if their **CONDITIONs** have become **_True_**.  
  If so, the **ACTIONS** will be executed once.  
  In order for the **RULE** to execute again, the **CONDITIONs** must become **_False_** before becoming **_True_** again.
- **Single-Event**  
  Single-Events are pre-defined events like the following:
  - OnPlayerDied
  - OnPlayerDeployed
  - OnPlayerJoined

## Rule Contexts

Every rule has a certain context it runs in.

The available contexts are:

- **Global**
- **Player**
- **Team**
- **Vehicle**
- **CapturePoint**
- **MCOM**

This is useful as you can use certain payloads of the event and only write the conditions and actions once, but it will be executed for every object of the context.

E.g. a rule in the player context will be evaluated per player and tick. The team-context evaluates for every team in the game (usually team 1 and team 2, but can also include team 0).
Whereas a rule in the global context is only evaluated once for the global game state.

## Event Payloads

Within the **Player** and **Team** contexts, payload value blocks, such as **EventPlayer** and **EventTeam**,
can be used to refer to the specific **Player** or **Team** within the **EVENT**

E.g. the rule for the event **OnPlayerEarnedKill** in the _player_ **_context_**, which will trigger when a
**Player** earns a kill against another **Player** holds the following event-_Payloads_:

- **EventPlayer** (Killer)
- **EventOtherPlayer** (Victim)
- **EventDeathType** (Victim Death Type)
- **EventWeapon** (Killing Weapon)

## Conditions

Conditions are logical checks which must evaluate to "true" in order for the actions of the rule to be executed.
You can place multiple conditions to a rule, which will connect them with a logical "AND".

If you want to have an OR operator in conditions, you would have to use an "OR-block" within one condition.

Conditions are evaluated in parrallel or at least and depending on the result of upper condition blocks.
This means that if one condition fails, the remaining conditions are still being evaluated.

If you have the conditions in a player context rule checking the status of the player being alive and the distance to an objective being closer than 5 meter, this could cause issues in the error log.

Why?

A players distance to an objective can't be determined if they are not alive and in the deployment screen.
If a player is in the deployment screen, the distance condition would still be evaluated even if the "isAlive" condition is not met.

## Actions

The Actions section of a rule block contains all the blocks that will be executed if the conditions of the rule were met.
The blocks will be executed in sequential order from top to bottom.
