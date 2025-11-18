---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / SetRedeployTime

# Function: SetRedeployTime()

```ts
function SetRedeployTime(player, redeployTime): void;
```

Defined in: [mod/index.d.ts:20359](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20359)

Overrides the time to redeploy for a target player. The redeploy time must be set to a value between 0 and 60 seconds.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `redeployTime` | `number` |

## Returns

`void`
