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

Defined in: [mod/index.d.ts:14076](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L14076)

This will trigger when a Player interacts with an UI button.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventUIWidget` | [`UIWidget`](../../UIWidget/_index.md) |
| `eventUIButtonEvent` | [`UIButtonEvent`](../../UIButtonEvent/_index.md) |

## Returns

`void`
