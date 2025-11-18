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

Defined in: [mod/index.d.ts:20716](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20716)

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

Defined in: [mod/index.d.ts:20719](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20719)

Restricts a world icon to be visible only to a specific Player or Team.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `worldIcon` | [`WorldIcon`](../WorldIcon/_index.md) |
| `newPlayerOwner` | [`Player`](../Player/_index.md) |

### Returns

`void`
