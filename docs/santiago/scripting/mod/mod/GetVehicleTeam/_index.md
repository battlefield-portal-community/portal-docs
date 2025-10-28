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

Defined in: [mod/index.d.ts:15881](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15881)

Returns the team of the provided vehicle. Note: A vehicle that is not occupied will have a neutral team.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |

## Returns

[`Team`](../Team/_index.md)
