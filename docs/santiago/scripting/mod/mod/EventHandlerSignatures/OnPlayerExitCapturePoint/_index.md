---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../../_index.md) / [mod](../../../_index.md) / [mod](../../_index.md) / [EventHandlerSignatures](../_index.md) / OnPlayerExitCapturePoint

# Function: OnPlayerExitCapturePoint()

```ts
function OnPlayerExitCapturePoint(eventPlayer, eventCapturePoint): void;
```

Defined in: [mod/index.d.ts:22271](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L22271)

This will trigger when a Player exits a CapturePoint capturing area.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventCapturePoint` | [`CapturePoint`](../../CapturePoint/_index.md) |

## Returns

`void`
