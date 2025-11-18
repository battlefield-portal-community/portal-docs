---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / Heal

# Function: Heal()

## Call Signature

```ts
function Heal(player, healAmount): void;
```

Defined in: [mod/index.d.ts:20461](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20461)

Instantly adds a given amount of health to the target player. Can optionally specify healing player.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `healAmount` | `number` |

### Returns

`void`

## Call Signature

```ts
function Heal(
   player, 
   healAmount, 
   giver): void;
```

Defined in: [mod/index.d.ts:20464](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20464)

Instantly adds a given amount of health to the target player. Can optionally specify healing player.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `healAmount` | `number` |
| `giver` | [`Player`](../Player/_index.md) |

### Returns

`void`

## Call Signature

```ts
function Heal(vehicle, repairAmount): void;
```

Defined in: [mod/index.d.ts:20467](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20467)

Instantly adds a given amount of health to the target player. Can optionally specify healing player.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |
| `repairAmount` | `number` |

### Returns

`void`
