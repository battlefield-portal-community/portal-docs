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

Defined in: [mod/index.d.ts:12577](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12577)

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

Defined in: [mod/index.d.ts:12580](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12580)

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

Defined in: [mod/index.d.ts:12583](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12583)

Displays a message on the world log above the minimap for 6 seconds. If no target is provided, it will display the message to everyone.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | [`Message`](../Message/_index.md) |
| `team` | [`Team`](../Team/_index.md) |

### Returns

`void`
