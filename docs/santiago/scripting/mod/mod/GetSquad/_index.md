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

Defined in: [mod/index.d.ts:13657](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13657)

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

Defined in: [mod/index.d.ts:13660](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13660)

Returns the squad object corresponding to the provided player, or team/squad id.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `teamIdNumber` | `number` |
| `squadIdNumber` | `number` |

### Returns

[`Squad`](../Squad/_index.md)
