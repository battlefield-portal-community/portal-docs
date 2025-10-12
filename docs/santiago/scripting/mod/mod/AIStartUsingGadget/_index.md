---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / AIStartUsingGadget

# Function: AIStartUsingGadget()

## Call Signature

```ts
function AIStartUsingGadget(
   player, 
   gadget, 
   targetPos): void;
```

Defined in: [mod/index.d.ts:12011](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12011)

Gives a player the instruction to use a specific gadget on a target location or player. (Only works for AI players)

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `gadget` | [`UnguidedRocketLauncher`](../OpenGadgets/_index.md#unguidedrocketlauncher) |
| `targetPos` | [`Vector`](../Vector/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AIStartUsingGadget(
   player, 
   gadget, 
   targetPlayer): void;
```

Defined in: [mod/index.d.ts:12014](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12014)

Gives a player the instruction to use a specific gadget on a target location or player. (Only works for AI players)

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `gadget` | [`UnguidedRocketLauncher`](../OpenGadgets/_index.md#unguidedrocketlauncher) |
| `targetPlayer` | [`Player`](../Player/_index.md) |

### Returns

`void`
