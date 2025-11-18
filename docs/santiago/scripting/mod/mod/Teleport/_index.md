---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / Teleport

# Function: Teleport()

## Call Signature

```ts
function Teleport(
   player, 
   destination, 
   orientation): void;
```

Defined in: [mod/index.d.ts:20544](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20544)

Teleports a target to a provided valid position facing a specified angle (in radians).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `destination` | [`Vector`](../Vector/_index.md) |
| `orientation` | `number` |

### Returns

`void`

## Call Signature

```ts
function Teleport(
   vehicle, 
   destination, 
   orientation): void;
```

Defined in: [mod/index.d.ts:20547](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20547)

Teleports a target to a provided valid position facing a specified angle (in radians).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |
| `destination` | [`Vector`](../Vector/_index.md) |
| `orientation` | `number` |

### Returns

`void`
