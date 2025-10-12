---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / MoveVFX

# Function: MoveVFX()

```ts
function MoveVFX(
   vfxID, 
   position, 
   rotation): void;
```

Defined in: [mod/index.d.ts:12140](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12140)

Move a VFX to a new coordinate. May have become redundant with the creation of the universal MoveObject action.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `vfxID` | [`VFX`](../VFX/_index.md) |
| `position` | [`Vector`](../Vector/_index.md) |
| `rotation` | [`Vector`](../Vector/_index.md) |

## Returns

`void`
