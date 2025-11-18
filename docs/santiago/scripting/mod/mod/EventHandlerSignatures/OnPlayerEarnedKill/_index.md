---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../../_index.md) / [mod](../../../_index.md) / [mod](../../_index.md) / [EventHandlerSignatures](../_index.md) / OnPlayerEarnedKill

# Function: OnPlayerEarnedKill()

```ts
function OnPlayerEarnedKill(
   eventPlayer, 
   eventOtherPlayer, 
   eventDeathType, 
   eventWeaponUnlock): void;
```

Defined in: [mod/index.d.ts:22241](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L22241)

This will trigger when a Player earns a kill against another Player.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventOtherPlayer` | [`Player`](../../Player/_index.md) |
| `eventDeathType` | [`DeathType`](../../DeathType/_index.md) |
| `eventWeaponUnlock` | [`WeaponUnlock`](../../WeaponUnlock/_index.md) |

## Returns

`void`
