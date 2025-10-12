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

Defined in: [mod/index.d.ts:12316](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12316)

Gradually modifies the value of a Variable at a specified rate (value/second) until it reaches the provided limit.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `variable` | [`Variable`](../Variable/_index.md) |
| `limit` | `number` |
| `deltaPerSecond` | `number` |

## Returns

`void`
