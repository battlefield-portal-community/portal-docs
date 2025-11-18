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

Defined in: [mod/index.d.ts:21499](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21499)

Returns a copy of an array with the provided value appended to the end.  Note: It is not possible for an array to contain arrays. Attempting to append an array to an array will concatenate them instead.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `array` | [`Array`](../Array/_index.md) |
| `value` | `any` |

## Returns

[`Array`](../Array/_index.md)
