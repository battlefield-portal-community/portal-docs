---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / EndGameMode

# Function: EndGameMode()

## Call Signature

```ts
function EndGameMode(player): void;
```

Defined in: [mod/index.d.ts:13681](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13681)

Ends the current gamemode and designates the provided Player or Team as the winner. The gamemode ends in draw if Team is set to 0.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |

### Returns

`void`

## Call Signature

```ts
function EndGameMode(team): void;
```

Defined in: [mod/index.d.ts:13684](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13684)

Ends the current gamemode and designates the provided Player or Team as the winner. The gamemode ends in draw if Team is set to 0.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `team` | [`Team`](../Team/_index.md) |

### Returns

`void`
