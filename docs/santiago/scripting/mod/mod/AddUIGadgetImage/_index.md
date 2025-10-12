---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / AddUIGadgetImage

# Function: AddUIGadgetImage()

## Call Signature

```ts
function AddUIGadgetImage(
   name, 
   position, 
   size, 
   anchor, 
   gadget, 
   parent): void;
```

Defined in: [mod/index.d.ts:12886](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12886)

Creates a new UI Image Widget based on a Gadget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `gadget` | [`Gadgets`](../Gadgets/_index.md) |
| `parent` | [`UIWidget`](../UIWidget/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIGadgetImage(
   name, 
   position, 
   size, 
   anchor, 
   gadget, 
   parent, 
   visibility): void;
```

Defined in: [mod/index.d.ts:12896](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12896)

Creates a new UI Image Widget based on a Gadget.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `name` | `string` |
| `position` | [`Vector`](../Vector/_index.md) |
| `size` | [`Vector`](../Vector/_index.md) |
| `anchor` | [`UIAnchor`](../UIAnchor/_index.md) |
| `gadget` | [`Gadgets`](../Gadgets/_index.md) |
| `parent` | [`UIWidget`](../UIWidget/_index.md) |
| `visibility` | [`Player`](../Player/_index.md) \| [`Team`](../Team/_index.md) |

### Returns

`void`
