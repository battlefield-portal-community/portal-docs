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

Defined in: [mod/index.d.ts:15197](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15197)

Returns a sorted version of the specified Array given a Number value to sort by (ascending). CurrentArrayElement can be utilized to represent each value in the Array. In the following example, CurrentArrayElement is used to represent each Player in AllPlayers. GetGameModeScore is used with CurrentArrayElement to return the score, used as a rank, to sort the Array in ascending order.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `array` | [`Array`](../Array/_index.md) |
| `index` | `number` |

## Returns

[`Array`](../Array/_index.md)
