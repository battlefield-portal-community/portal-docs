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

Defined in: [mod/index.d.ts:13815](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13815)

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

Defined in: [mod/index.d.ts:13818](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13818)

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

Defined in: [mod/index.d.ts:13821](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13821)

Instantly adds a given amount of health to the target player. Can optionally specify healing player.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |
| `repairAmount` | `number` |

### Returns

`void`
