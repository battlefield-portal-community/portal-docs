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

Defined in: [mod/index.d.ts:13830](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13830)

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

Defined in: [mod/index.d.ts:13833](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13833)

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

Defined in: [mod/index.d.ts:13841](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13841)

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

Defined in: [mod/index.d.ts:13844](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13844)

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

Defined in: [mod/index.d.ts:13847](https://github.com/battlefield-portal-community/portal-docs/blob/ff09b2690670f74de7e97198022e5a97ff1161ff/generators/santiago/mod/index.d.ts#L13847)

Spots a target Player for all players for a specified duration of time (in seconds).

### Parameters

| Parameter | Type |
| ------ | ------ |
| `targetplayer` | [`Player`](../Player/_index.md) |
| `duration` | `number` |

### Returns

`void`
