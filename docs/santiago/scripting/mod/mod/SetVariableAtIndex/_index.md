---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / SetVariableAtIndex

# Function: SetVariableAtIndex()

```ts
function SetVariableAtIndex(
   arrayVariable, 
   arrayIndex, 
   value): void;
```

Defined in: [mod/index.d.ts:12023](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12023)

Finds or initializes an Array on a provided Variable, and stores a provided value in that Array at the specified index.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `arrayVariable` | [`Variable`](../Variable/_index.md) |
| `arrayIndex` | `number` |
| `value` | `any` |

## Returns

`void`
