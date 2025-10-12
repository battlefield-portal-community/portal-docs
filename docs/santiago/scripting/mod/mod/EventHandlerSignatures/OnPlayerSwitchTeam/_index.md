---
draft: false
type: typedoc_gen
---

[**Battlefield 6 Scripting Docs**](../../../../_index.md)

***

[Battlefield 6 Scripting Docs](../../../../_index.md) / [mod](../../../_index.md) / [mod](../../_index.md) / [EventHandlerSignatures](../_index.md) / OnPlayerSwitchTeam

# Function: OnPlayerSwitchTeam()

```ts
function OnPlayerSwitchTeam(eventPlayer, eventTeam): void;
```

Defined in: [mod/index.d.ts:14073](https://github.com/battlefield-portal-community/portal-docs/blob/6d87e21c5922a3efb03c634dbe98e5fe6e797672/generators/santiago/mod/index.d.ts#L14073)

This will trigger when a Player changes team.

## Parameters

| Parameter | Type |
| ------ | ------ |
| `eventPlayer` | [`Player`](../../Player/_index.md) |
| `eventTeam` | [`Team`](../../Team/_index.md) |

## Returns

`void`
