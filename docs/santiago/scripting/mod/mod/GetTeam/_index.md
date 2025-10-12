---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / GetTeam

# Function: GetTeam()

## Call Signature

```ts
function GetTeam(player): Team;
```

Defined in: [mod/index.d.ts:13663](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13663)

Returns the team value of the specified player OR the corresponding team of the provided number.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |

### Returns

[`Team`](../Team/_index.md)

## Call Signature

```ts
function GetTeam(teamId): Team;
```

Defined in: [mod/index.d.ts:13666](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L13666)

Returns the team value of the specified player OR the corresponding team of the provided number.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `teamId` | `number` |

### Returns

[`Team`](../Team/_index.md)
