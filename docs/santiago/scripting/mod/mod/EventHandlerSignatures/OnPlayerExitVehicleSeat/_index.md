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

Defined in: [mod/index.d.ts:16045](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L16045)

This will trigger when a Player exits a Vehicle seat.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventVehicle` | [`Vehicle`](../../Vehicle/_index.md) |
| `eventSeat` | [`Object`](../../Object/_index.md) |

## Returns

`void`
