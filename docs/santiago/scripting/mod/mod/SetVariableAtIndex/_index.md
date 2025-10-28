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

Defined in: [mod/index.d.ts:13123](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13123)

Finds or initializes an Array on a provided Variable, and stores a provided value in that Array at the specified index.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `arrayVariable` | [`Variable`](../Variable/_index.md) |
| `arrayIndex` | `number` |
| `value` | `any` |

## Returns

`void`
