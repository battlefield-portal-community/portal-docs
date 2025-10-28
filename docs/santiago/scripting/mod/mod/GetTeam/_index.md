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

Defined in: [mod/index.d.ts:15566](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15566)

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

Defined in: [mod/index.d.ts:15569](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15569)

Returns the team value of the specified player OR the corresponding team of the provided number.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `teamId` | `number` |

### Returns

[`Team`](../Team/_index.md)
