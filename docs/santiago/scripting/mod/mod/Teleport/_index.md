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

Defined in: [mod/index.d.ts:12361](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12361)

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

Defined in: [mod/index.d.ts:12364](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12364)

Teleports a target to a provided valid position facing a specified angle (in radians).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |
| `destination` | [`Vector`](../Vector/_index.md) |
| `orientation` | `number` |

### Returns

`void`
