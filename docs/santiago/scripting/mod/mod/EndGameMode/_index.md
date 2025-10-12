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

Defined in: [mod/index.d.ts:12215](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12215)

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

Defined in: [mod/index.d.ts:12218](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12218)

Ends the current gamemode and designates the provided Player or Team as the winner. The gamemode ends in draw if Team is set to 0.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `team` | [`Team`](../Team/_index.md) |

### Returns

`void`
