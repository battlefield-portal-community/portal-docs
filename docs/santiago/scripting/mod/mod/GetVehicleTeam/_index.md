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

Defined in: [mod/index.d.ts:22115](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L22115)

Returns the team of the provided vehicle. Note: A vehicle that is not occupied will have a neutral team.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |

## Returns

[`Team`](../Team/_index.md)
