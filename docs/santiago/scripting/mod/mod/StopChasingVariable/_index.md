---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / StopChasingVariable

# Function: StopChasingVariable()

```ts
function StopChasingVariable(variable): void;
```

Defined in: [mod/index.d.ts:12322](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12322)

Stops an in-progress tracking of a Variable from the ChaseVariableOverTime or ChaseVariableAtRate blocks, leaving it at its current value.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `variable` | [`Variable`](../Variable/_index.md) |

## Returns

`void`
