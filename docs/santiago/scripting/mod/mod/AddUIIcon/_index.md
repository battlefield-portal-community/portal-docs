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

Defined in: [mod/index.d.ts:12493](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12493)

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

Defined in: [mod/index.d.ts:12503](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12503)

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
