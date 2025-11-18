---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / ChaseVariableOverTime

# Function: ChaseVariableOverTime()

```ts
function ChaseVariableOverTime(
   variable, 
   limit, 
   durationSeconds): void;
```

Defined in: [mod/index.d.ts:20499](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20499)

Gradually modifies the value of a Variable over time (in seconds). The variable's value will reach the limit at the end of the interval.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `variable` | [`Variable`](../Variable/_index.md) |
| `limit` | `number` |
| `durationSeconds` | `number` |

## Returns

`void`
