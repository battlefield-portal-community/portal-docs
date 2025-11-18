---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../../_index.md) / [mod](../../../_index.md) / [mod](../../_index.md) / [EventHandlerSignatures](../_index.md) / OnPlayerUIButtonEvent

# Function: OnPlayerUIButtonEvent()

```ts
function OnPlayerUIButtonEvent(
   eventPlayer, 
   eventUIWidget, 
   eventUIButtonEvent): void;
```

Defined in: [mod/index.d.ts:22296](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L22296)

This will trigger when a Player interacts with an UI button.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventUIWidget` | [`UIWidget`](../../UIWidget/_index.md) |
| `eventUIButtonEvent` | [`UIButtonEvent`](../../UIButtonEvent/_index.md) |

## Returns

`void`
