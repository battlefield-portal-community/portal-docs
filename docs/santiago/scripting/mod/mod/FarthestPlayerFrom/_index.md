---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / FarthestPlayerFrom

# Function: FarthestPlayerFrom()

## Call Signature

```ts
function FarthestPlayerFrom(vector): Player;
```

Defined in: [mod/index.d.ts:15548](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15548)

Returns the farthest alive player from a provided position. Can be filtered using a team. Note: If no players are alive when this block is called, the returned player will be invalid.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vector` | [`Vector`](../Vector/_index.md) |

### Returns

[`Player`](../Player/_index.md)

## Call Signature

```ts
function FarthestPlayerFrom(vector, team): Player;
```

Defined in: [mod/index.d.ts:15551](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15551)

Returns the farthest alive player from a provided position. Can be filtered using a team. Note: If no players are alive when this block is called, the returned player will be invalid.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vector` | [`Vector`](../Vector/_index.md) |
| `team` | [`Team`](../Team/_index.md) |

### Returns

[`Player`](../Player/_index.md)
