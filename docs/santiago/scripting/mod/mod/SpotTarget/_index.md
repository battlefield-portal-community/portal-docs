---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / SpotTarget

# Function: SpotTarget()

## Call Signature

```ts
function SpotTarget(
   targetplayer, 
   duration, 
   spotStatus): void;
```

Defined in: [mod/index.d.ts:20476](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20476)

Spots a target Player for all players for a specified duration of time (in seconds).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `targetplayer` | [`Player`](../Player/_index.md) |
| `duration` | `number` |
| `spotStatus` | [`SpotStatus`](../SpotStatus/_index.md) |

### Returns

`void`

## Call Signature

```ts
function SpotTarget(
   targetPlayer, 
   spotterPlayer, 
   duration, 
   spotStatus): void;
```

Defined in: [mod/index.d.ts:20479](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20479)

Spots a target Player for all players for a specified duration of time (in seconds).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `targetPlayer` | [`Player`](../Player/_index.md) |
| `spotterPlayer` | [`Player`](../Player/_index.md) |
| `duration` | `number` |
| `spotStatus` | [`SpotStatus`](../SpotStatus/_index.md) |

### Returns

`void`

## Call Signature

```ts
function SpotTarget(targetplayer, spotStatus): void;
```

Defined in: [mod/index.d.ts:20487](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20487)

Spots a target Player for all players for a specified duration of time (in seconds).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `targetplayer` | [`Player`](../Player/_index.md) |
| `spotStatus` | [`SpotStatus`](../SpotStatus/_index.md) |

### Returns

`void`

## Call Signature

```ts
function SpotTarget(
   targetPlayer, 
   spotterPlayer, 
   duration): void;
```

Defined in: [mod/index.d.ts:20490](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20490)

Spots a target Player for all players for a specified duration of time (in seconds).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `targetPlayer` | [`Player`](../Player/_index.md) |
| `spotterPlayer` | [`Player`](../Player/_index.md) |
| `duration` | `number` |

### Returns

`void`

## Call Signature

```ts
function SpotTarget(targetplayer, duration): void;
```

Defined in: [mod/index.d.ts:20493](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20493)

Spots a target Player for all players for a specified duration of time (in seconds).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `targetplayer` | [`Player`](../Player/_index.md) |
| `duration` | `number` |

### Returns

`void`
