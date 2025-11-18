---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / OrbitObjectOverTime

# Function: OrbitObjectOverTime()

## Call Signature

```ts
function OrbitObjectOverTime(
   object, 
   orbitTransform, 
   timeInSeconds, 
   radius, 
   shouldLoop, 
   shouldReverse, 
   clockwise): void;
```

Defined in: [mod/index.d.ts:20638](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20638)

Orbits the Object around the provided transform over time. Optional orbitAxis otherwise transform's up vector is used

### Parameters

| Parameter | Type |
| ------ | ------ |
| `object` | [`Object`](../Object/_index.md) |
| `orbitTransform` | [`Transform`](../Transform/_index.md) |
| `timeInSeconds` | `number` |
| `radius` | `number` |
| `shouldLoop` | `boolean` |
| `shouldReverse` | `boolean` |
| `clockwise` | `boolean` |

### Returns

`void`

## Call Signature

```ts
function OrbitObjectOverTime(
   object, 
   orbitTransform, 
   timeInSeconds, 
   radius, 
   shouldLoop, 
   shouldReverse, 
   clockwise, 
   orbitAxis): void;
```

Defined in: [mod/index.d.ts:20649](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20649)

Orbits the Object around the provided transform over time. Optional orbitAxis otherwise transform's up vector is used

### Parameters

| Parameter | Type |
| ------ | ------ |
| `object` | [`Object`](../Object/_index.md) |
| `orbitTransform` | [`Transform`](../Transform/_index.md) |
| `timeInSeconds` | `number` |
| `radius` | `number` |
| `shouldLoop` | `boolean` |
| `shouldReverse` | `boolean` |
| `clockwise` | `boolean` |
| `orbitAxis` | [`Vector`](../Vector/_index.md) |

### Returns

`void`
