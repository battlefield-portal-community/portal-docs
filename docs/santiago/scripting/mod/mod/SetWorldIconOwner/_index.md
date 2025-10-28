---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / SetWorldIconOwner

# Function: SetWorldIconOwner()

## Call Signature

```ts
function SetWorldIconOwner(worldIcon, newTeamOwner): void;
```

Defined in: [mod/index.d.ts:14399](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14399)

Restricts a world icon to be visible only to a specific Player or Team.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `worldIcon` | [`WorldIcon`](../WorldIcon/_index.md) |
| `newTeamOwner` | [`Team`](../Team/_index.md) |

### Returns

`void`

## Call Signature

```ts
function SetWorldIconOwner(worldIcon, newPlayerOwner): void;
```

Defined in: [mod/index.d.ts:14402](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L14402)

Restricts a world icon to be visible only to a specific Player or Team.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `worldIcon` | [`WorldIcon`](../WorldIcon/_index.md) |
| `newPlayerOwner` | [`Player`](../Player/_index.md) |

### Returns

`void`
