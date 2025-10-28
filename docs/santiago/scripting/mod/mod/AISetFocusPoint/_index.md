---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / AISetFocusPoint

# Function: AISetFocusPoint()

```ts
function AISetFocusPoint(
   player, 
   point, 
   isTarget): void;
```

Defined in: [mod/index.d.ts:13096](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13096)

Sets a player's focus point, possibly asking it to fire at it. (Only works for AI players)

## Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `point` | [`Vector`](../Vector/_index.md) |
| `isTarget` | `boolean` |

## Returns

`void`
