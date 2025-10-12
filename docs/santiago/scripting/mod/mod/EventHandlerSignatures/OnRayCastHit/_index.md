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

Defined in: [mod/index.d.ts:14086](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L14086)

This will trigger when a Raycast hits a target.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventPoint` | [`Vector`](../../Vector/_index.md) |
| `eventNormal` | [`Vector`](../../Vector/_index.md) |

## Returns

`void`
