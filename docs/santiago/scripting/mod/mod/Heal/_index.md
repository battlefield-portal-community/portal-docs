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

Defined in: [mod/index.d.ts:12281](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12281)

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

Defined in: [mod/index.d.ts:12284](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12284)

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

Defined in: [mod/index.d.ts:12287](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L12287)

Instantly adds a given amount of health to the target player. Can optionally specify healing player.

### Parameters

| Parameter | Type |
| ------ | ------ |
| `vehicle` | [`Vehicle`](../Vehicle/_index.md) |
| `repairAmount` | `number` |

### Returns

`void`
