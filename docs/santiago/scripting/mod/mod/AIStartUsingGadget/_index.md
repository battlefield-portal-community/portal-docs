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

Defined in: [mod/index.d.ts:20125](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20125)

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

Defined in: [mod/index.d.ts:20128](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20128)

Gives a player the instruction to use a specific gadget on a target location or player. (Only works for AI players)

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `gadget` | [`UnguidedRocketLauncher`](../OpenGadgets/_index.md#unguidedrocketlauncher) |
| `targetPlayer` | [`Player`](../Player/_index.md) |

### Returns

`void`
