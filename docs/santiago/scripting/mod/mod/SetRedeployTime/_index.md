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

Defined in: [mod/index.d.ts:13672](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13672)

Overrides the time to redeploy for a target player. The redeploy time must be set to a value between 0 and 60 seconds.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `redeployTime` | `number` |

## Returns

`void`
