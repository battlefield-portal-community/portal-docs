---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / AddUIText

# Function: AddUIText()

## Call Signature

```ts
function AddUIText(
   name, 
   position, 
   size, 
   anchor, 
   message): void;
```

Defined in: [mod/index.d.ts:12998](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12998)

Creates a new UI Text Widget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `message` | [`Message`](../Message/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIText(
   name, 
   position, 
   size, 
   anchor, 
   message, 
   receiver): void;
```

Defined in: [mod/index.d.ts:13001](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13001)

Creates a new UI Text Widget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `message` | [`Message`](../Message/_index.md) |
| `receiver` | [`Player`](../Player/_index.md) \| [`Team`](../Team/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIText(
   name, 
   position, 
   size, 
   anchor, 
   parent, 
   visible, 
   padding, 
   bgColor, 
   bgAlpha, 
   bgFill, 
   message, 
   textSize, 
   textColor, 
   textAlpha, 
   textAnchor): void;
```

Defined in: [mod/index.d.ts:13011](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13011)

Creates a new UI Text Widget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `parent` | [`UIWidget`](../UIWidget/_index.md) |
| `visible` | `boolean` |
| `padding` | `number` |
| `bgColor` | [`Vector`](../Vector/_index.md) |
| `bgAlpha` | `number` |
| `bgFill` | [`UIBgFill`](../UIBgFill/_index.md) |
| `message` | [`Message`](../Message/_index.md) |
| `textSize` | `number` |
| `textColor` | [`Vector`](../Vector/_index.md) |
| `textAlpha` | `number` |
| `textAnchor` | [`UIAnchor`](../UIAnchor/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIText(
   name, 
   position, 
   size, 
   anchor, 
   parent, 
   visible, 
   padding, 
   bgColor, 
   bgAlpha, 
   bgFill, 
   message, 
   textSize, 
   textColor, 
   textAlpha, 
   textAnchor, 
   receiver): void;
```

Defined in: [mod/index.d.ts:13030](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13030)

Creates a new UI Text Widget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `parent` | [`UIWidget`](../UIWidget/_index.md) |
| `visible` | `boolean` |
| `padding` | `number` |
| `bgColor` | [`Vector`](../Vector/_index.md) |
| `bgAlpha` | `number` |
| `bgFill` | [`UIBgFill`](../UIBgFill/_index.md) |
| `message` | [`Message`](../Message/_index.md) |
| `textSize` | `number` |
| `textColor` | [`Vector`](../Vector/_index.md) |
| `textAlpha` | `number` |
| `textAnchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `receiver` | [`Player`](../Player/_index.md) \| [`Team`](../Team/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIText(
   name, 
   position, 
   size, 
   anchor, 
   parent, 
   visible, 
   padding, 
   bgColor, 
   bgAlpha, 
   bgFill, 
   message, 
   textSize, 
   textColor, 
   textAlpha, 
   textAnchor, 
   depth): void;
```

Defined in: [mod/index.d.ts:13050](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13050)

Creates a new UI Text Widget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `parent` | [`UIWidget`](../UIWidget/_index.md) |
| `visible` | `boolean` |
| `padding` | `number` |
| `bgColor` | [`Vector`](../Vector/_index.md) |
| `bgAlpha` | `number` |
| `bgFill` | [`UIBgFill`](../UIBgFill/_index.md) |
| `message` | [`Message`](../Message/_index.md) |
| `textSize` | `number` |
| `textColor` | [`Vector`](../Vector/_index.md) |
| `textAlpha` | `number` |
| `textAnchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `depth` | [`UIDepth`](../UIDepth/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIText(
   name, 
   position, 
   size, 
   anchor, 
   parent, 
   visible, 
   padding, 
   bgColor, 
   bgAlpha, 
   bgFill, 
   message, 
   textSize, 
   textColor, 
   textAlpha, 
   textAnchor, 
   depth, 
   receiver): void;
```

Defined in: [mod/index.d.ts:13070](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13070)

Creates a new UI Text Widget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `parent` | [`UIWidget`](../UIWidget/_index.md) |
| `visible` | `boolean` |
| `padding` | `number` |
| `bgColor` | [`Vector`](../Vector/_index.md) |
| `bgAlpha` | `number` |
| `bgFill` | [`UIBgFill`](../UIBgFill/_index.md) |
| `message` | [`Message`](../Message/_index.md) |
| `textSize` | `number` |
| `textColor` | [`Vector`](../Vector/_index.md) |
| `textAlpha` | `number` |
| `textAnchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `depth` | [`UIDepth`](../UIDepth/_index.md) |
| `receiver` | [`Player`](../Player/_index.md) \| [`Team`](../Team/_index.md) |

### Returns

`void`
