---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../_index.md)

***

[Battlefield 6 Scripting Docs](../../_index.md) / [modlib](../_index.md) / IfThenElse

# Function: IfThenElse()

```ts
function IfThenElse<T>(
   condition, 
   ifTrue, 
   ifFalse): T;
```

Defined in: [modlib/index.ts:64](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/modlib/index.ts#L64)

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
