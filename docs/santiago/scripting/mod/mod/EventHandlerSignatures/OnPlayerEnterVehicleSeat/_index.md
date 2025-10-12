---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../../_index.md) / [mod](../../../_index.md) / [mod](../../_index.md) / [EventHandlerSignatures](../_index.md) / OnPlayerEnterVehicleSeat

# Function: OnPlayerEnterVehicleSeat()

```ts
function OnPlayerEnterVehicleSeat(
   eventPlayer, 
   eventVehicle, 
   eventSeat): void;
```

Defined in: [mod/index.d.ts:14041](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L14041)

This will trigger when a Player enters a Vehicle seat.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventVehicle` | [`Vehicle`](../../Vehicle/_index.md) |
| `eventSeat` | [`Object`](../../Object/_index.md) |

## Returns

`void`
