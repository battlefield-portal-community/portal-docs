---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / GetSquad

# Function: GetSquad()

## Call Signature

```ts
function GetSquad(player): Squad;
```

Defined in: [mod/index.d.ts:21872](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21872)

Returns the squad object corresponding to the provided player, or team/squad id.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |

### Returns

[`Squad`](../Squad/_index.md)

## Call Signature

```ts
function GetSquad(teamIdNumber, squadIdNumber): Squad;
```

Defined in: [mod/index.d.ts:21875](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21875)

Returns the squad object corresponding to the provided player, or team/squad id.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `teamIdNumber` | `number` |
| `squadIdNumber` | `number` |

### Returns

[`Squad`](../Squad/_index.md)
