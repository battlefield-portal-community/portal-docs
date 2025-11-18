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

Defined in: [mod/index.d.ts:20763](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20763)

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

Defined in: [mod/index.d.ts:20766](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20766)

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

Defined in: [mod/index.d.ts:20769](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20769)

Displays a message on the world log above the minimap for 6 seconds. If no target is provided, it will display the message to everyone.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | [`Message`](../Message/_index.md) |
| `team` | [`Team`](../Team/_index.md) |

### Returns

`void`
