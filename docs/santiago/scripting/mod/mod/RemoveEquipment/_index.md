---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / RemoveEquipment

# Function: RemoveEquipment()

## Call Signature

```ts
function RemoveEquipment(player, inventorySlot): void;
```

Defined in: [mod/index.d.ts:13943](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13943)

Removes a Weapon or Gadget from a Soldier's loadout.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `inventorySlot` | [`InventorySlots`](../InventorySlots/_index.md) |

### Returns

`void`

## Call Signature

```ts
function RemoveEquipment(arg0, weapon): void;
```

Defined in: [mod/index.d.ts:13946](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13946)

Removes a Weapon or Gadget from a Soldier's loadout.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `arg0` | [`Player`](../Player/_index.md) |
| `weapon` | [`Weapons`](../Weapons/_index.md) |

### Returns

`void`

## Call Signature

```ts
function RemoveEquipment(arg0, gadget): void;
```

Defined in: [mod/index.d.ts:13949](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13949)

Removes a Weapon or Gadget from a Soldier's loadout.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `arg0` | [`Player`](../Player/_index.md) |
| `gadget` | [`Gadgets`](../Gadgets/_index.md) |

### Returns

`void`
