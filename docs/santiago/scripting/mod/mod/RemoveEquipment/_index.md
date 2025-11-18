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

Defined in: [mod/index.d.ts:20592](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20592)

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

Defined in: [mod/index.d.ts:20595](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20595)

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

Defined in: [mod/index.d.ts:20598](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20598)

Removes a Weapon or Gadget from a Soldier's loadout.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `arg0` | [`Player`](../Player/_index.md) |
| `gadget` | [`Gadgets`](../Gadgets/_index.md) |

### Returns

`void`
