---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / GetTeam

# Function: GetTeam()

## Call Signature

```ts
function GetTeam(player): Team;
```

Defined in: [mod/index.d.ts:21878](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21878)

Returns the team value of the specified player OR the corresponding team of the provided number.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |

### Returns

[`Team`](../Team/_index.md)

## Call Signature

```ts
function GetTeam(teamId): Team;
```

Defined in: [mod/index.d.ts:21881](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21881)

Returns the team value of the specified player OR the corresponding team of the provided number.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `teamId` | `number` |

### Returns

[`Team`](../Team/_index.md)
