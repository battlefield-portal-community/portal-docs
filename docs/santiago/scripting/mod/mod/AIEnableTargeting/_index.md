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

Defined in: [mod/index.d.ts:11979](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L11979)

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

Defined in: [mod/index.d.ts:11982](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L11982)

Enables or disables targeting for AI. An AI unable to target cannot shoot, but will also not notice other soldiers (Only works for AI players)

### Parameters

| Parameter | Type |
| ------ | ------ |
| `player` | [`Player`](../Player/_index.md) |
| `enable` | `boolean` |

### Returns

`void`
