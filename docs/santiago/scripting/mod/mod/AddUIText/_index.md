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

Defined in: [mod/index.d.ts:21184](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21184)

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

Defined in: [mod/index.d.ts:21187](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21187)

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

Defined in: [mod/index.d.ts:21197](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21197)

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

Defined in: [mod/index.d.ts:21216](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21216)

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

Defined in: [mod/index.d.ts:21236](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21236)

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

Defined in: [mod/index.d.ts:21256](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21256)

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
