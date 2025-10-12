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

Defined in: [mod/index.d.ts:12530](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12530)

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

Defined in: [mod/index.d.ts:12533](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12533)

Restricts a world icon to be visible only to a specific Player or Team.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `worldIcon` | [`WorldIcon`](../WorldIcon/_index.md) |
| `newPlayerOwner` | [`Player`](../Player/_index.md) |

### Returns

`void`
