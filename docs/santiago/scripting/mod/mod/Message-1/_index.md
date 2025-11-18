---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / Message

# Function: Message()

## Call Signature

```ts
function Message(
   msg, 
   msgArg0, 
   msgArg1, 
   msgArg2): Message;
```

Defined in: [mod/index.d.ts:21977](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21977)

Returns a constructed message object which can be used with event game mode message, notification message, highlighted game mode message, and custom notification message. The message object is created by providing a number, player, or format string (which can take up to 3 format items).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `msg` | `string` \| `number` \| [`Player`](../Player/_index.md) |
| `msgArg0` | `string` \| `number` \| [`Player`](../Player/_index.md) |
| `msgArg1` | `string` \| `number` \| [`Player`](../Player/_index.md) |
| `msgArg2` | `string` \| `number` \| [`Player`](../Player/_index.md) |

### Returns

[`Message`](../Message/_index.md)

## Call Signature

```ts
function Message(
   msg, 
   msgArg0, 
   msgArg1): Message;
```

Defined in: [mod/index.d.ts:21985](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21985)

Returns a constructed message object which can be used with event game mode message, notification message, highlighted game mode message, and custom notification message. The message object is created by providing a number, player, or format string (which can take up to 3 format items).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `msg` | `string` \| `number` \| [`Player`](../Player/_index.md) |
| `msgArg0` | `string` \| `number` \| [`Player`](../Player/_index.md) |
| `msgArg1` | `string` \| `number` \| [`Player`](../Player/_index.md) |

### Returns

[`Message`](../Message/_index.md)

## Call Signature

```ts
function Message(msg, msgArg0): Message;
```

Defined in: [mod/index.d.ts:21992](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21992)

Returns a constructed message object which can be used with event game mode message, notification message, highlighted game mode message, and custom notification message. The message object is created by providing a number, player, or format string (which can take up to 3 format items).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `msg` | `string` \| `number` \| [`Player`](../Player/_index.md) |
| `msgArg0` | `string` \| `number` \| [`Player`](../Player/_index.md) |

### Returns

[`Message`](../Message/_index.md)

## Call Signature

```ts
function Message(msg): Message;
```

Defined in: [mod/index.d.ts:21995](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21995)

Returns a constructed message object which can be used with event game mode message, notification message, highlighted game mode message, and custom notification message. The message object is created by providing a number, player, or format string (which can take up to 3 format items).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `msg` | `string` \| `number` \| [`Player`](../Player/_index.md) |

### Returns

[`Message`](../Message/_index.md)
