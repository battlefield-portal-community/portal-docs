---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / AIDefendPositionBehavior

# Function: AIDefendPositionBehavior()

```ts
function AIDefendPositionBehavior(
   player, 
   defendPosition, 
   minDistance, 
   maxDistance): void;
```

Defined in: [mod/index.d.ts:20028](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20028)

Sets a player to defend an area around a location. (Only works for AI players)

## Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `defendPosition` | [`Vector`](../Vector/_index.md) |
| `minDistance` | `number` |
| `maxDistance` | `number` |

## Returns

`void`
