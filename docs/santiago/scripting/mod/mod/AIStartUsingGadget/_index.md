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

Defined in: [mod/index.d.ts:13111](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13111)

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

Defined in: [mod/index.d.ts:13114](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13114)

Gives a player the instruction to use a specific gadget on a target location or player. (Only works for AI players)

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `gadget` | [`UnguidedRocketLauncher`](../OpenGadgets/_index.md#unguidedrocketlauncher) |
| `targetPlayer` | [`Player`](../Player/_index.md) |

### Returns

`void`
