---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / GetVehicleTeam

# Function: GetVehicleTeam()

```ts
function GetVehicleTeam(vehicle): Team;
```

Defined in: [mod/index.d.ts:13897](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13897)

Returns the team of the provided vehicle. Note: A vehicle that is not occupied will have a neutral team.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |

## Returns

[`Team`](../Team/_index.md)
