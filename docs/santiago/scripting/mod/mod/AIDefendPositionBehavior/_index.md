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

Defined in: [mod/index.d.ts:13014](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13014)

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
