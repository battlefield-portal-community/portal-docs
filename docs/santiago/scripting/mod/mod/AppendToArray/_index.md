---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / AppendToArray

# Function: AppendToArray()

```ts
function AppendToArray(array, value): Array;
```

Defined in: [mod/index.d.ts:15173](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15173)

Returns a copy of an array with the provided value appended to the end.  Note: It is not possible for an array to contain arrays. Attempting to append an array to an array will concatenate them instead.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `array` | [`Array`](../Array/_index.md) |
| `value` | `any` |

## Returns

[`Array`](../Array/_index.md)
