---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / SetPlayerMaxHealth

# Function: SetPlayerMaxHealth()

```ts
function SetPlayerMaxHealth(player, maxHealth): void;
```

Defined in: [mod/index.d.ts:12427](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12427)

Sets the max health of a target player from 0 to 1000.  The value will be multiplied by the max health multiplier of the that target.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `maxHealth` | `number` |

## Returns

`void`
