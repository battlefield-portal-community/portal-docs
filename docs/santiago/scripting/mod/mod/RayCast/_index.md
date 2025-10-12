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

Defined in: [mod/index.d.ts:12257](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12257)

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

Defined in: [mod/index.d.ts:12260](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12260)

Request the system to evaluate if a straight line between two points is interupted or not. Use OnRayCastHit and OnRayCastMissed to read the result.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `start` | [`Vector`](../Vector/_index.md) |
| `stop` | [`Vector`](../Vector/_index.md) |

### Returns

`void`
