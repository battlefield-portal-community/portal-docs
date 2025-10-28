---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / SpawnObject

# Function: SpawnObject()

## Call Signature

```ts
function SpawnObject(
   prefabEnum, 
   position, 
   rotation, 
   scale): any;
```

Defined in: [mod/index.d.ts:15307](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15307)

Spawns an object at runtime. Returns an object id if the object supports it, otherwise -1

### Parameters

| Parameter | Type |
| ------ | ------ |
| `prefabEnum` | \| [`RuntimeSpawn_Common`](../RuntimeSpawn_Common/_index.md) \| [`RuntimeSpawn_Abbasid`](../RuntimeSpawn_Abbasid/_index.md) \| [`RuntimeSpawn_Aftermath`](../RuntimeSpawn_Aftermath/_index.md) \| [`RuntimeSpawn_Badlands`](../RuntimeSpawn_Badlands/_index.md) \| [`RuntimeSpawn_Battery`](../RuntimeSpawn_Battery/_index.md) \| [`RuntimeSpawn_Capstone`](../RuntimeSpawn_Capstone/_index.md) \| [`RuntimeSpawn_Dumbo`](../RuntimeSpawn_Dumbo/_index.md) \| [`RuntimeSpawn_FireStorm`](../RuntimeSpawn_FireStorm/_index.md) \| [`RuntimeSpawn_Limestone`](../RuntimeSpawn_Limestone/_index.md) \| [`RuntimeSpawn_Outskirts`](../RuntimeSpawn_Outskirts/_index.md) \| [`RuntimeSpawn_Tungsten`](../RuntimeSpawn_Tungsten/_index.md) |
| `position` | [`Vector`](../Vector/_index.md) |
| `rotation` | [`Vector`](../Vector/_index.md) |
| `scale` | [`Vector`](../Vector/_index.md) |

### Returns

`any`

## Call Signature

```ts
function SpawnObject(
   prefabEnum, 
   position, 
   rotation): any;
```

Defined in: [mod/index.d.ts:15326](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L15326)

Spawns an object at runtime. Returns an object id if the object supports it, otherwise -1

### Parameters

| Parameter | Type |
| ------ | ------ |
| `prefabEnum` | \| [`RuntimeSpawn_Common`](../RuntimeSpawn_Common/_index.md) \| [`RuntimeSpawn_Abbasid`](../RuntimeSpawn_Abbasid/_index.md) \| [`RuntimeSpawn_Aftermath`](../RuntimeSpawn_Aftermath/_index.md) \| [`RuntimeSpawn_Badlands`](../RuntimeSpawn_Badlands/_index.md) \| [`RuntimeSpawn_Battery`](../RuntimeSpawn_Battery/_index.md) \| [`RuntimeSpawn_Capstone`](../RuntimeSpawn_Capstone/_index.md) \| [`RuntimeSpawn_Dumbo`](../RuntimeSpawn_Dumbo/_index.md) \| [`RuntimeSpawn_FireStorm`](../RuntimeSpawn_FireStorm/_index.md) \| [`RuntimeSpawn_Limestone`](../RuntimeSpawn_Limestone/_index.md) \| [`RuntimeSpawn_Outskirts`](../RuntimeSpawn_Outskirts/_index.md) \| [`RuntimeSpawn_Tungsten`](../RuntimeSpawn_Tungsten/_index.md) |
| `position` | [`Vector`](../Vector/_index.md) |
| `rotation` | [`Vector`](../Vector/_index.md) |

### Returns

`any`
