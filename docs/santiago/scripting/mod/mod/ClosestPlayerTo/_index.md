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

Defined in: [mod/index.d.ts:13639](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13639)

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

Defined in: [mod/index.d.ts:13642](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13642)

Returns the closest alive player to a provided position. Can be filtered using a team. Note: If no players are alive when this block is called, the returned player will be invalid.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vector` | [`Vector`](../Vector/_index.md) |
| `team` | [`Team`](../Team/_index.md) |

### Returns

[`Player`](../Player/_index.md)
