---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / DisplayCustomNotificationMessage

# Function: DisplayCustomNotificationMessage()

## Call Signature

```ts
function DisplayCustomNotificationMessage(
   msg, 
   slot, 
   duration): void;
```

Defined in: [mod/index.d.ts:12554](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12554)

Display a custom notification in one of the slots for the specified team or player.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `msg` | [`Message`](../Message/_index.md) |
| `slot` | [`CustomNotificationSlots`](../CustomNotificationSlots/_index.md) |
| `duration` | `number` |

### Returns

`void`

## Call Signature

```ts
function DisplayCustomNotificationMessage(
   msg, 
   slot, 
   duration, 
   target): void;
```

Defined in: [mod/index.d.ts:12561](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12561)

Display a custom notification in one of the slots for the specified team or player.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `msg` | [`Message`](../Message/_index.md) |
| `slot` | [`CustomNotificationSlots`](../CustomNotificationSlots/_index.md) |
| `duration` | `number` |
| `target` | [`Player`](../Player/_index.md) |

### Returns

`void`

## Call Signature

```ts
function DisplayCustomNotificationMessage(
   msg, 
   slot, 
   duration, 
   target): void;
```

Defined in: [mod/index.d.ts:12569](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12569)

Display a custom notification in one of the slots for the specified team or player.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `msg` | [`Message`](../Message/_index.md) |
| `slot` | [`CustomNotificationSlots`](../CustomNotificationSlots/_index.md) |
| `duration` | `number` |
| `target` | [`Team`](../Team/_index.md) |

### Returns

`void`
