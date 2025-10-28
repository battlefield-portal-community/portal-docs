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

Defined in: [mod/index.d.ts:13895](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13895)

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

Defined in: [mod/index.d.ts:13898](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13898)

Teleports a target to a provided valid position facing a specified angle (in radians).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |
| `destination` | [`Vector`](../Vector/_index.md) |
| `orientation` | `number` |

### Returns

`void`
