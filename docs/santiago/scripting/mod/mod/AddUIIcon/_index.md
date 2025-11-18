---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / AddUIIcon

# Function: AddUIIcon()

## Call Signature

```ts
function AddUIIcon(
   parentObject, 
   image, 
   verticalOffset, 
   iconColour, 
   iconText, 
   visibility): void;
```

Defined in: [mod/index.d.ts:20679](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20679)

Attaches a new UI Icon Widget to an object.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `parentObject` | [`Object`](../Object/_index.md) |
| `image` | [`WorldIconImages`](../WorldIconImages/_index.md) |
| `verticalOffset` | `number` |
| `iconColour` | [`Vector`](../Vector/_index.md) |
| `iconText` | [`Message`](../Message/_index.md) |
| `visibility` | [`Player`](../Player/_index.md) \| [`Team`](../Team/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AddUIIcon(
   parentObject, 
   image, 
   verticalOffset, 
   iconColour, 
   iconText): void;
```

Defined in: [mod/index.d.ts:20689](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20689)

Attaches a new UI Icon Widget to an object.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `parentObject` | [`Object`](../Object/_index.md) |
| `image` | [`WorldIconImages`](../WorldIconImages/_index.md) |
| `verticalOffset` | `number` |
| `iconColour` | [`Vector`](../Vector/_index.md) |
| `iconText` | [`Message`](../Message/_index.md) |

### Returns

`void`
