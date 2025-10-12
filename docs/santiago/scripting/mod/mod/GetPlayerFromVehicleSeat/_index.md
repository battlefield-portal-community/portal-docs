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

Defined in: [mod/index.d.ts:13909](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13909)

Returns the player currently occupying the provided seat index number of the provided vehicle. Note: If no players are in the vehicle seat when this block is called, the returned player will be invalid.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |
| `number` | `number` |

## Returns

[`Player`](../Player/_index.md)
