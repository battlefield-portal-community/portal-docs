---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / SetPlayerIncomingDamageFactor

# Function: SetPlayerIncomingDamageFactor()

```ts
function SetPlayerIncomingDamageFactor(player, amount): void;
```

Defined in: [mod/index.d.ts:20541](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20541)

Sets damage taken factor on player (Will be rounded to the nearest 5%). The value will be clamped between 0 - 200%.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `amount` | `number` |

## Returns

`void`
