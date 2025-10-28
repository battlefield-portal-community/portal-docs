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

Defined in: [mod/index.d.ts:15743](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15743)

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

Defined in: [mod/index.d.ts:15751](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15751)

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

Defined in: [mod/index.d.ts:15758](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15758)

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

Defined in: [mod/index.d.ts:15761](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15761)

Returns a constructed message object which can be used with event game mode message, notification message, highlighted game mode message, and custom notification message. The message object is created by providing a number, player, or format string (which can take up to 3 format items).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `msg` | `string` \| `number` \| [`Player`](../Player/_index.md) |

### Returns

[`Message`](../Message/_index.md)
