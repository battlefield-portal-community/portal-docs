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

Defined in: [mod/index.d.ts:12206](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12206)

Overrides the time to redeploy for a target player. The redeploy time must be set to a value between 0 and 60 seconds.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `redeployTime` | `number` |

## Returns

`void`
