---
title: "Rule"
draft: false
---
**RULE** blocks are triggered from an in-game **EVENT**. When an **EVENT** triggers, this block will check if its **CONDITION** has been met and then execute all of the **ACTIONS**.  
**Types of **RULE** Blocks Events**
**Ongoing**
Ongoing **EVENT** types continually check if its **CONDITION** has become **_True_**. If so, the **ACTIONS** will be executed once. In order for the **EVENT** to execute again, the **CONDITION** must become **_False_** before becoming **_True_** again.  
   
Ongoing **EVENT** types currently exist within the context of:  
  
- **Global**  
- **Player**  
- **Team**  
- **Vehicle**  
- **CapturePoint**  
  
Within the **Player** and **Team** contexts, payload value blocks, such as **EventPlayer** and **EventTeam**, can be used to refer to the specific **Player** or **Team** within the **EVENT**. _Note: In FFA, Ongoing **Team** will not execute at all._
**OnPlayerDied**
This will trigger whenever a **Player** dies. _Payloads: **EventPlayer** (Victim), **EventOtherPlayer** (Killer), **EventDeathType** (Victim Death Type), **EventWeapon** (Killing Weapon)_
**OnPlayerDeployed**
This will trigger whenever a **Player** deploys. _Payloads: **EventPlayer** (Deployed Player)_
**OnPlayerJoinGame**
This will trigger when a **Player** joins the game. _Payloads: **EventPlayer** (Joined Player)_
**OnPlayerLeaveGame**
This will trigger when any player leaves the game.
**OnPlayerEarnedKill**
This will trigger when a **Player** earns a kill against another **Player**. _Payloads: **EventPlayer** (Killer), **EventOtherPlayer** (Victim), **EventDeathType** (Victim Death Type), **EventWeapon** (Killing Weapon)_
**OnGameModeEnding**
This will trigger when the gamemode ends.
**OnMandown**
This will trigger when a **Player** is forced into the mandown state. _Payloads: **EventPlayer**  (Downed Player)_
**OnRevived**
This will trigger when a **Player** is revived by another **Player**. _Payloads: **EventPlayer** (Revived Player), **EventOtherPlayer** (Reviver Player)_
**OnTimeLimitReached**
This will trigger when the gamemode time limit has been reached.
**OnGameModeStarted**
This will trigger at the start of the gamemode.
**OnPlayerUndeploy**
This will trigger when the **Player** dies and returns to the deploy screen. _Payloads: **EventPlayer** (Dead Player)_
**OnVehicleDeployed**
This will trigger when a **Vehicle** is called into the map. _Payloads: **EventVehicle** (Spawned Vehicle)_
**OnVehicleDestroyed**
This will trigger when a **Vehicle** is destroyed. _Payloads: **EventVehicle** (Destroyed Vehicle)_
**OnPlayerEnterVehicle**
This will trigger when a **Player** enters a **Vehicle**. _Payloads: **EventPlayer** (Player Who Enters), **EventVehicle** (Vehicle)_
**OnPlayerExitVehicle**
This will trigger when a **Player** exits a **Vehicle**. _Payloads: **EventPlayer** (Player Who Exits), **EventVehicle** (Vehicle)_
**OnPlayerEnterVehicleSeat**
This will trigger when a **Player** enters a **Vehicle** seat. _Payloads: **EventPlayer** (Player Who Enters Seat), **EventVehicle** (Vehicle), **EventSeat** (Seat Index)_
**OnPlayerExitVehicleSeat**
This will trigger when a **Player** exits a **Vehicle** seat. _Payloads: **EventPlayer** (Player Who Exits Seat), **EventVehicle** (Vehicle), **EventSeat** (Seat Index)_
**OnCapturePointCaptured**
This will trigger when a team takes control of a **CapturePoint**. _Payloads: **EventCapturePoint** (Captured Capture Point)_
**OnCapturePointCapturing**
This will trigger when a team begins capturing a **CapturePoint**. _Payloads: **EventCapturePoint** (Capture Point Being Captured)_
**OnCapturePointLost**
This will trigger when a team loses control of a **CapturePoint**. _Payloads: **EventCapturePoint** (Lost Capture Point)_
**OnCapturePointNeutralizing**
This will trigger when a team begins neutralizing a **CapturePoint**. _Payloads: **EventCapturePoint** (Capture Point Being Neutralized)_
**OnPlayerEnterCapturePoint**
This will trigger when a **Player** enters a **CapturePoint** capturing area. _Payloads: **EventPlayer** (Player Entering Capture Area), **EventCapturePoint** (Capture Point Being Entered)_
**OnPlayerExitCapturePoint**
This will trigger when a **Player** exits a **CapturePoint** capturing area. _Payloads: **EventPlayer** (Player Exiting Capture Area), **EventCapturePoint** (Capture Point Being Exited)_
**OnMCOMArmed**
This will trigger when a **MCOM** is armed. _Payloads: **EventMCOM** (Armed MCOM), **EventPlayer** (Player Who Armed)_
**OnMCOMDefused**
This will trigger when a **MCOM** is defused. _Payloads: **EventMCOM** (Defused MCOM), **EventPlayer** (Player Who Defused)_
**OnMCOMDestroyed**
This will trigger when a **MCOM** is destroyed. _Payloads: **EventMCOM** (Destroyed MCOM)_
**OnPlayerDamaged**
This will trigger when a **Player** takes damage. _Payloads: **EventPlayer** (Damaged Player), **EventOtherPlayer** (Damager Player), **EventDamageType** (Damage Type), **EventWeapon** (Damager Weapon)_
**OnPlayerEarnKillAssist**
This will trigger when a **Player** earns a kill assist. _Payloads: **EventPlayer** (Assist Player), **EventOtherPlayer** (Victim)

![Rule](https://raw.githubusercontent.com/battlefield-portal-community/Image-CDN/main/portal_blocks/Rule.png)