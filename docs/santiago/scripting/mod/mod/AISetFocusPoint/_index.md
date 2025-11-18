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

Defined in: [mod/index.d.ts:20110](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20110)

Sets a player's focus point, possibly asking it to fire at it. (Only works for AI players)

## Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `point` | [`Vector`](../Vector/_index.md) |
| `isTarget` | `boolean` |

## Returns

`void`
