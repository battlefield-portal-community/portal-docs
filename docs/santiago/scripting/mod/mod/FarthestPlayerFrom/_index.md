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

Defined in: [mod/index.d.ts:21860](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21860)

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

Defined in: [mod/index.d.ts:21863](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21863)

Returns the farthest alive player from a provided position. Can be filtered using a team. Note: If no players are alive when this block is called, the returned player will be invalid.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vector` | [`Vector`](../Vector/_index.md) |
| `team` | [`Team`](../Team/_index.md) |

### Returns

[`Player`](../Player/_index.md)
