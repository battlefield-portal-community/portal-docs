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

Defined in: [mod/index.d.ts:20740](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20740)

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

Defined in: [mod/index.d.ts:20747](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20747)

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

Defined in: [mod/index.d.ts:20755](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20755)

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
