---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../../_index.md) / [mod](../../../_index.md) / [mod](../../_index.md) / [EventHandlerSignatures](../_index.md) / OnPlayerDied

# Function: OnPlayerDied()

```ts
function OnPlayerDied(
   eventPlayer, 
   eventOtherPlayer, 
   eventDeathType, 
   eventWeaponUnlock): void;
```

Defined in: [mod/index.d.ts:14013](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L14013)

This will trigger whenever a Player dies.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventOtherPlayer` | [`Player`](../../Player/_index.md) |
| `eventDeathType` | [`DeathType`](../../DeathType/_index.md) |
| `eventWeaponUnlock` | [`WeaponUnlock`](../../WeaponUnlock/_index.md) |

## Returns

`void`
