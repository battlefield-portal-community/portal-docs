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

Defined in: [mod/index.d.ts:11996](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L11996)

Sets a player's focus point, possibly asking it to fire at it. (Only works for AI players)

## Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `point` | [`Vector`](../Vector/_index.md) |
| `isTarget` | `boolean` |

## Returns

`void`
