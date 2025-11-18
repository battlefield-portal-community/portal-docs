---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../_index.md) / [mod](../../_index.md) / [mod](../_index.md) / AIEnableTargeting

# Function: AIEnableTargeting()

## Call Signature

```ts
function AIEnableTargeting(player): void;
```

Defined in: [mod/index.d.ts:20093](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20093)

Enables or disables targeting for AI. An AI unable to target cannot shoot, but will also not notice other soldiers (Only works for AI players)

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |

### Returns

`void`

## Call Signature

```ts
function AIEnableTargeting(player, enable): void;
```

Defined in: [mod/index.d.ts:20096](https://github.com/battlefield-portal-community/portal-docs/blob/e47049b63e51188248b798c13df021a40e9a89fc/generators/santiago/mod/index.d.ts#L20096)

Enables or disables targeting for AI. An AI unable to target cannot shoot, but will also not notice other soldiers (Only works for AI players)

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `enable` | `boolean` |

### Returns

`void`
