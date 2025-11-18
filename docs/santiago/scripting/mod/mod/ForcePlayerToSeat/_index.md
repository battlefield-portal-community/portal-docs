---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / ForcePlayerToSeat

# Function: ForcePlayerToSeat()

```ts
function ForcePlayerToSeat(
   player, 
   vehicle, 
   seatNumber): void;
```

Defined in: [mod/index.d.ts:21480](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21480)

Forces the specified player into the target vehicle at the provided seat number.  If the provided seat is -1, that player will be forced into the first available seat.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |
| `seatNumber` | `number` |

## Returns

`void`
