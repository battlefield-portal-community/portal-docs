---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / AddUIContainer

# Function: AddUIContainer()

## Call Signature

```ts
function AddUIContainer(
   name, 
   position, 
   size, 
   anchor): void;
```

Defined in: [mod/index.d.ts:12814](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12814)

Creates a new UI Container Widget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIContainer(
   name, 
   position, 
   size, 
   anchor, 
   receiver): void;
```

Defined in: [mod/index.d.ts:12817](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12817)

Creates a new UI Container Widget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `receiver` | [`Player`](../Player/_index.md) \| [`Team`](../Team/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIContainer(
   name, 
   position, 
   size, 
   anchor, 
   parent, 
   visible, 
   padding, 
   bgColor, 
   bgAlpha, 
   bgFill): void;
```

Defined in: [mod/index.d.ts:12826](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12826)

Creates a new UI Container Widget.

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

### Returns

`void`

## Call Signature

```ts
function AddUIContainer(
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
   receiver): void;
```

Defined in: [mod/index.d.ts:12840](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12840)

Creates a new UI Container Widget.

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
| `receiver` | [`Player`](../Player/_index.md) \| [`Team`](../Team/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIContainer(
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
   depth): void;
```

Defined in: [mod/index.d.ts:12855](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12855)

Creates a new UI Container Widget.

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
| `depth` | [`UIDepth`](../UIDepth/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIContainer(
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
   depth, 
   receiver): void;
```

Defined in: [mod/index.d.ts:12870](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12870)

Creates a new UI Container Widget.

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
| `depth` | [`UIDepth`](../UIDepth/_index.md) |
| `receiver` | [`Player`](../Player/_index.md) \| [`Team`](../Team/_index.md) |

### Returns

`void`
