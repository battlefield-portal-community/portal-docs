---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../../_index.md) / [mod](../../../_index.md) / [mod](../../_index.md) / [EventHandlerSignatures](../_index.md) / OnPlayerDamaged

# Function: OnPlayerDamaged()

```ts
function OnPlayerDamaged(
   eventPlayer, 
   eventOtherPlayer, 
   eventDamageType, 
   eventWeaponUnlock): void;
```

Defined in: [mod/index.d.ts:22222](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L22222)

This will trigger when a Player takes damage.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventOtherPlayer` | [`Player`](../../Player/_index.md) |
| `eventDamageType` | [`DamageType`](../../DamageType/_index.md) |
| `eventWeaponUnlock` | [`WeaponUnlock`](../../WeaponUnlock/_index.md) |

## Returns

`void`
