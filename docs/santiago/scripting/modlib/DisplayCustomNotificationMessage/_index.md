---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../_index.md)

***

[Battlefield 6 Scripting Docs](../../_index.md) / [modlib](../_index.md) / DisplayCustomNotificationMessage

# Function: DisplayCustomNotificationMessage()

```ts
function DisplayCustomNotificationMessage(
   msg, 
   custom, 
   duration, 
   target?): void;
```

Defined in: [modlib/index.ts:523](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/modlib/index.ts#L523)

## Parameters

| Parameter | Type |
| ------ | ------ |
| `msg` | [`Message`](../../mod/mod/Message/_index.md) |
| `custom` | [`CustomNotificationSlots`](../../mod/mod/CustomNotificationSlots/_index.md) |
| `duration` | `number` |
| `target?` | \| [`Player`](../../mod/mod/Player/_index.md) \| [`Team`](../../mod/mod/Team/_index.md) |

## Returns

`void`
