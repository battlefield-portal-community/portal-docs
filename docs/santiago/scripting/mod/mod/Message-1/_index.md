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

Defined in: [mod/index.d.ts:13759](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13759)

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

Defined in: [mod/index.d.ts:13767](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13767)

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

Defined in: [mod/index.d.ts:13774](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13774)

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

Defined in: [mod/index.d.ts:13777](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13777)

Returns a constructed message object which can be used with event game mode message, notification message, highlighted game mode message, and custom notification message. The message object is created by providing a number, player, or format string (which can take up to 3 format items).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `msg` | `string` \| `number` \| [`Player`](../Player/_index.md) |

### Returns

[`Message`](../Message/_index.md)
