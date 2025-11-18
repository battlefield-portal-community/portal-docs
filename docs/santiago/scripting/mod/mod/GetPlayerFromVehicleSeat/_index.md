---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / GetPlayerFromVehicleSeat

# Function: GetPlayerFromVehicleSeat()

```ts
function GetPlayerFromVehicleSeat(vehicle, number): Player;
```

Defined in: [mod/index.d.ts:22127](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L22127)

Returns the player currently occupying the provided seat index number of the provided vehicle. Note: If no players are in the vehicle seat when this block is called, the returned player will be invalid.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |
| `number` | `number` |

## Returns

[`Player`](../Player/_index.md)
