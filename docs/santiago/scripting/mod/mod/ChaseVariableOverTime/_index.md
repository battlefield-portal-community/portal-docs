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

Defined in: [mod/index.d.ts:13853](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13853)

Gradually modifies the value of a Variable over time (in seconds). The variable's value will reach the limit at the end of the interval.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `variable` | [`Variable`](../Variable/_index.md) |
| `limit` | `number` |
| `durationSeconds` | `number` |

## Returns

`void`
