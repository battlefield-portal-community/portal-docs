---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / SortedArray

# Function: SortedArray()

```ts
function SortedArray(array, index): Array;
```

Defined in: [mod/index.d.ts:21523](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21523)

Returns a sorted version of the specified Array given a Number value to sort by (ascending). CurrentArrayElement can be utilized to represent each value in the Array. In the following example, CurrentArrayElement is used to represent each Player in AllPlayers. GetGameModeScore is used with CurrentArrayElement to return the score, used as a rank, to sort the Array in ascending order.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `array` | [`Array`](../Array/_index.md) |
| `index` | `number` |

## Returns

[`Array`](../Array/_index.md)
