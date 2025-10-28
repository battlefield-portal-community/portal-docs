---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / ChaseVariableAtRate

# Function: ChaseVariableAtRate()

```ts
function ChaseVariableAtRate(
   variable, 
   limit, 
   deltaPerSecond): void;
```

Defined in: [mod/index.d.ts:13850](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13850)

Gradually modifies the value of a Variable at a specified rate (value/second) until it reaches the provided limit.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `variable` | [`Variable`](../Variable/_index.md) |
| `limit` | `number` |
| `deltaPerSecond` | `number` |

## Returns

`void`
