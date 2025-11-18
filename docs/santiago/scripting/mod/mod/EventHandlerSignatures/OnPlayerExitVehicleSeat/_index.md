---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../../_index.md) / [mod](../../../_index.md) / [mod](../../_index.md) / [EventHandlerSignatures](../_index.md) / OnPlayerExitVehicleSeat

# Function: OnPlayerExitVehicleSeat()

```ts
function OnPlayerExitVehicleSeat(
   eventPlayer, 
   eventVehicle, 
   eventSeat): void;
```

Defined in: [mod/index.d.ts:22277](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L22277)

This will trigger when a Player exits a Vehicle seat.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventVehicle` | [`Vehicle`](../../Vehicle/_index.md) |
| `eventSeat` | [`Object`](../../Object/_index.md) |

## Returns

`void`
