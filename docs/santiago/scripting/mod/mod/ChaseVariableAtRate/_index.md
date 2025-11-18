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

Defined in: [mod/index.d.ts:20496](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20496)

Gradually modifies the value of a Variable at a specified rate (value/second) until it reaches the provided limit.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `variable` | [`Variable`](../Variable/_index.md) |
| `limit` | `number` |
| `deltaPerSecond` | `number` |

## Returns

`void`
