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

Defined in: [mod/index.d.ts:20368](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20368)

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

Defined in: [mod/index.d.ts:20371](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20371)

Ends the current gamemode and designates the provided Player or Team as the winner. The gamemode ends in draw if Team is set to 0.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `team` | [`Team`](../Team/_index.md) |

### Returns

`void`
