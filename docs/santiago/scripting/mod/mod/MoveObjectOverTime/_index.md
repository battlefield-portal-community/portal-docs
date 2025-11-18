---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / MoveObjectOverTime

# Function: MoveObjectOverTime()

```ts
function MoveObjectOverTime(
   object, 
   positionDelta, 
   rotationDelta, 
   timeInSeconds, 
   shouldLoop, 
   shouldReverse): void;
```

Defined in: [mod/index.d.ts:20628](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20628)

Moves the Object by the delta position and rotation over the time provided. Options to loop indefinitely and reverse

## Parameters

| Parameter | Type |
| ------ | ------ |
| `object` | [`Object`](../Object/_index.md) |
| `positionDelta` | [`Vector`](../Vector/_index.md) |
| `rotationDelta` | [`Vector`](../Vector/_index.md) |
| `timeInSeconds` | `number` |
| `shouldLoop` | `boolean` |
| `shouldReverse` | `boolean` |

## Returns

`void`
