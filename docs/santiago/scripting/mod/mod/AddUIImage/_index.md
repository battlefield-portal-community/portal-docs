---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / AddUIImage

# Function: AddUIImage()

## Call Signature

```ts
function AddUIImage(
   name, 
   position, 
   size, 
   anchor, 
   imageType): void;
```

Defined in: [mod/index.d.ts:12907](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12907)

Creates a new UI Image Widget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `imageType` | [`UIImageType`](../UIImageType/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIImage(
   name, 
   position, 
   size, 
   anchor, 
   imageType, 
   receiver): void;
```

Defined in: [mod/index.d.ts:12916](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12916)

Creates a new UI Image Widget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `imageType` | [`UIImageType`](../UIImageType/_index.md) |
| `receiver` | [`Player`](../Player/_index.md) \| [`Team`](../Team/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIImage(
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
   imageType, 
   imageColor, 
   imageAlpha): void;
```

Defined in: [mod/index.d.ts:12926](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12926)

Creates a new UI Image Widget.

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
| `imageType` | [`UIImageType`](../UIImageType/_index.md) |
| `imageColor` | [`Vector`](../Vector/_index.md) |
| `imageAlpha` | `number` |

### Returns

`void`

## Call Signature

```ts
function AddUIImage(
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
   imageType, 
   imageColor, 
   imageAlpha, 
   receiver): void;
```

Defined in: [mod/index.d.ts:12943](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12943)

Creates a new UI Image Widget.

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
| `imageType` | [`UIImageType`](../UIImageType/_index.md) |
| `imageColor` | [`Vector`](../Vector/_index.md) |
| `imageAlpha` | `number` |
| `receiver` | [`Player`](../Player/_index.md) \| [`Team`](../Team/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIImage(
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
   imageType, 
   imageColor, 
   imageAlpha, 
   depth): void;
```

Defined in: [mod/index.d.ts:12961](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12961)

Creates a new UI Image Widget.

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
| `imageType` | [`UIImageType`](../UIImageType/_index.md) |
| `imageColor` | [`Vector`](../Vector/_index.md) |
| `imageAlpha` | `number` |
| `depth` | [`UIDepth`](../UIDepth/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIImage(
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
   imageType, 
   imageColor, 
   imageAlpha, 
   depth, 
   receiver): void;
```

Defined in: [mod/index.d.ts:12979](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12979)

Creates a new UI Image Widget.

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
| `imageType` | [`UIImageType`](../UIImageType/_index.md) |
| `imageColor` | [`Vector`](../Vector/_index.md) |
| `imageAlpha` | `number` |
| `depth` | [`UIDepth`](../UIDepth/_index.md) |
| `receiver` | [`Player`](../Player/_index.md) \| [`Team`](../Team/_index.md) |

### Returns

`void`
