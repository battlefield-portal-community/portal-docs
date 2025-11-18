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

Defined in: [mod/index.d.ts:21607](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21607)

Spawns an object at runtime. Returns an object id if the object supports it, otherwise -1

### Parameters

| Parameter | Type |
| ------ | ------ |
| `prefabEnum` | \| [`RuntimeSpawn_Common`](../RuntimeSpawn_Common/_index.md) \| [`RuntimeSpawn_Granite_ResidentialNorth`](../RuntimeSpawn_Granite_ResidentialNorth/_index.md) \| [`RuntimeSpawn_Abbasid`](../RuntimeSpawn_Abbasid/_index.md) \| [`RuntimeSpawn_Aftermath`](../RuntimeSpawn_Aftermath/_index.md) \| [`RuntimeSpawn_Badlands`](../RuntimeSpawn_Badlands/_index.md) \| [`RuntimeSpawn_Battery`](../RuntimeSpawn_Battery/_index.md) \| [`RuntimeSpawn_Capstone`](../RuntimeSpawn_Capstone/_index.md) \| [`RuntimeSpawn_Dumbo`](../RuntimeSpawn_Dumbo/_index.md) \| [`RuntimeSpawn_Eastwood`](../RuntimeSpawn_Eastwood/_index.md) \| [`RuntimeSpawn_FireStorm`](../RuntimeSpawn_FireStorm/_index.md) \| [`RuntimeSpawn_Limestone`](../RuntimeSpawn_Limestone/_index.md) \| [`RuntimeSpawn_Outskirts`](../RuntimeSpawn_Outskirts/_index.md) \| [`RuntimeSpawn_Tungsten`](../RuntimeSpawn_Tungsten/_index.md) \| [`RuntimeSpawn_Granite_Downtown`](../RuntimeSpawn_Granite_Downtown/_index.md) \| [`RuntimeSpawn_Granite_Marina`](../RuntimeSpawn_Granite_Marina/_index.md) \| [`RuntimeSpawn_Granite_TechCenter`](../RuntimeSpawn_Granite_TechCenter/_index.md) \| [`RuntimeSpawn_Sand`](../RuntimeSpawn_Sand/_index.md) |
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

Defined in: [mod/index.d.ts:21632](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L21632)

Spawns an object at runtime. Returns an object id if the object supports it, otherwise -1

### Parameters

| Parameter | Type |
| ------ | ------ |
| `prefabEnum` | \| [`RuntimeSpawn_Common`](../RuntimeSpawn_Common/_index.md) \| [`RuntimeSpawn_Granite_ResidentialNorth`](../RuntimeSpawn_Granite_ResidentialNorth/_index.md) \| [`RuntimeSpawn_Abbasid`](../RuntimeSpawn_Abbasid/_index.md) \| [`RuntimeSpawn_Aftermath`](../RuntimeSpawn_Aftermath/_index.md) \| [`RuntimeSpawn_Badlands`](../RuntimeSpawn_Badlands/_index.md) \| [`RuntimeSpawn_Battery`](../RuntimeSpawn_Battery/_index.md) \| [`RuntimeSpawn_Capstone`](../RuntimeSpawn_Capstone/_index.md) \| [`RuntimeSpawn_Dumbo`](../RuntimeSpawn_Dumbo/_index.md) \| [`RuntimeSpawn_Eastwood`](../RuntimeSpawn_Eastwood/_index.md) \| [`RuntimeSpawn_FireStorm`](../RuntimeSpawn_FireStorm/_index.md) \| [`RuntimeSpawn_Limestone`](../RuntimeSpawn_Limestone/_index.md) \| [`RuntimeSpawn_Outskirts`](../RuntimeSpawn_Outskirts/_index.md) \| [`RuntimeSpawn_Tungsten`](../RuntimeSpawn_Tungsten/_index.md) \| [`RuntimeSpawn_Granite_Downtown`](../RuntimeSpawn_Granite_Downtown/_index.md) \| [`RuntimeSpawn_Granite_Marina`](../RuntimeSpawn_Granite_Marina/_index.md) \| [`RuntimeSpawn_Granite_TechCenter`](../RuntimeSpawn_Granite_TechCenter/_index.md) \| [`RuntimeSpawn_Sand`](../RuntimeSpawn_Sand/_index.md) |
| `position` | [`Vector`](../Vector/_index.md) |
| `rotation` | [`Vector`](../Vector/_index.md) |

### Returns

`any`
