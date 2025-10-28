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

Defined in: [mod/index.d.ts:14261](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14261)

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

Defined in: [mod/index.d.ts:14295](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14295)

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
