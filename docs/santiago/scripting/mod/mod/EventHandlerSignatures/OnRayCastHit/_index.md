---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../../_index.md) / [mod](../../../_index.md) / [mod](../../_index.md) / [EventHandlerSignatures](../_index.md) / OnRayCastHit

# Function: OnRayCastHit()

```ts
function OnRayCastHit(
   eventPlayer, 
   eventPoint, 
   eventNormal): void;
```

Defined in: [mod/index.d.ts:22306](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L22306)

This will trigger when a Raycast hits a target.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventPoint` | [`Vector`](../../Vector/_index.md) |
| `eventNormal` | [`Vector`](../../Vector/_index.md) |

## Returns

`void`
