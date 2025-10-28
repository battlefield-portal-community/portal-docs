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

Defined in: [mod/index.d.ts:14683](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14683)

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

Defined in: [mod/index.d.ts:14686](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14686)

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

Defined in: [mod/index.d.ts:14695](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14695)

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

Defined in: [mod/index.d.ts:14709](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14709)

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

Defined in: [mod/index.d.ts:14724](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14724)

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

Defined in: [mod/index.d.ts:14739](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14739)

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
