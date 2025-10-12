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

Defined in: [mod/index.d.ts:11914](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L11914)

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
