---
draft: false
type: typedoc_gen
---

[**bf6docs**](../../_index.md)

***

[bf6docs](../../_index.md) / [modlib](../_index.md) / IfThenElse

# Function: IfThenElse()

```ts
function IfThenElse<T>(
   condition, 
   ifTrue, 
   ifFalse): T;
```

Defined in: modlib/index.ts:64

## Type Parameters

| Type Parameter |
| ------ |
| `T` |

## Parameters

| Parameter | Type |
| ------ | ------ |
| `condition` | `boolean` |
| `ifTrue` | () => `T` |
| `ifFalse` | () => `T` |

## Returns

`T`
