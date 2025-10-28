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

Defined in: [mod/index.d.ts:14423](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14423)

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

Defined in: [mod/index.d.ts:14430](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14430)

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

Defined in: [mod/index.d.ts:14438](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14438)

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
