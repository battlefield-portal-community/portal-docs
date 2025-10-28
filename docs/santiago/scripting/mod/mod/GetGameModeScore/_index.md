---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / GetGameModeScore

# Function: GetGameModeScore()

## Call Signature

```ts
function GetGameModeScore(player): number;
```

Defined in: [mod/index.d.ts:15230](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15230)

Returns the current gamemode score of the provided player or team.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |

### Returns

`number`

## Call Signature

```ts
function GetGameModeScore(team): number;
```

Defined in: [mod/index.d.ts:15233](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15233)

Returns the current gamemode score of the provided player or team.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `team` | [`Team`](../Team/_index.md) |

### Returns

`number`
