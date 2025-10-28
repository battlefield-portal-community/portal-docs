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

Defined in: [mod/index.d.ts:15560](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15560)

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

Defined in: [mod/index.d.ts:15563](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15563)

Returns the squad object corresponding to the provided player, or team/squad id.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `teamIdNumber` | `number` |
| `squadIdNumber` | `number` |

### Returns

[`Squad`](../Squad/_index.md)
