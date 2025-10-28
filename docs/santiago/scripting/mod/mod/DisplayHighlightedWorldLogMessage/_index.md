---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / DisplayHighlightedWorldLogMessage

# Function: DisplayHighlightedWorldLogMessage()

## Call Signature

```ts
function DisplayHighlightedWorldLogMessage(message): void;
```

Defined in: [mod/index.d.ts:14446](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14446)

Displays a message on the world log above the minimap for 6 seconds. If no target is provided, it will display the message to everyone.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | [`Message`](../Message/_index.md) |

### Returns

`void`

## Call Signature

```ts
function DisplayHighlightedWorldLogMessage(message, player): void;
```

Defined in: [mod/index.d.ts:14449](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14449)

Displays a message on the world log above the minimap for 6 seconds. If no target is provided, it will display the message to everyone.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | [`Message`](../Message/_index.md) |
| `player` | [`Player`](../Player/_index.md) |

### Returns

`void`

## Call Signature

```ts
function DisplayHighlightedWorldLogMessage(message, team): void;
```

Defined in: [mod/index.d.ts:14452](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14452)

Displays a message on the world log above the minimap for 6 seconds. If no target is provided, it will display the message to everyone.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | [`Message`](../Message/_index.md) |
| `team` | [`Team`](../Team/_index.md) |

### Returns

`void`
