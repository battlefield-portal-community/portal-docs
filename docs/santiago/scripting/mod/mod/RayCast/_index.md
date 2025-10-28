---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / RayCast

# Function: RayCast()

## Call Signature

```ts
function RayCast(
   player, 
   start, 
   stop): void;
```

Defined in: [mod/index.d.ts:13732](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13732)

Request the system to evaluate if a straight line between two points is interupted or not. Use OnRayCastHit and OnRayCastMissed to read the result.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `start` | [`Vector`](../Vector/_index.md) |
| `stop` | [`Vector`](../Vector/_index.md) |

### Returns

`void`

## Call Signature

```ts
function RayCast(start, stop): void;
```

Defined in: [mod/index.d.ts:13735](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13735)

Request the system to evaluate if a straight line between two points is interupted or not. Use OnRayCastHit and OnRayCastMissed to read the result.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `start` | [`Vector`](../Vector/_index.md) |
| `stop` | [`Vector`](../Vector/_index.md) |

### Returns

`void`
