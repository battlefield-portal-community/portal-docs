---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / ClosestPlayerTo

# Function: ClosestPlayerTo()

## Call Signature

```ts
function ClosestPlayerTo(vector): Player;
```

Defined in: [mod/index.d.ts:15542](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15542)

Returns the closest alive player to a provided position. Can be filtered using a team. Note: If no players are alive when this block is called, the returned player will be invalid.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vector` | [`Vector`](../Vector/_index.md) |

### Returns

[`Player`](../Player/_index.md)

## Call Signature

```ts
function ClosestPlayerTo(vector, team): Player;
```

Defined in: [mod/index.d.ts:15545](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15545)

Returns the closest alive player to a provided position. Can be filtered using a team. Note: If no players are alive when this block is called, the returned player will be invalid.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vector` | [`Vector`](../Vector/_index.md) |
| `team` | [`Team`](../Team/_index.md) |

### Returns

[`Player`](../Player/_index.md)
