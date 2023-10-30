# %{ID_ARRIVAL_BLOCK_SETPLAYERDAMAGE}

%{help.setplayerdamage.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_PLAYER}

    %{help.common.contexts.target}

2. %{PYRITE_TYPE_NUMBER}
3. %{PYRITE_TYPE_PLAYER}

    %{help.common.contexts.giver}

    %{help.common.optional}

```
<block type="SetPlayerDamage">
    <value name="VALUE-0">
        <block type="EventPlayer"></block>
    </value>
    <value name="VALUE-1">
        <block type="Number">
            <field name="NUM">25</field>
        </block>
    </value>
    <value name="VALUE-2">
        <block type="EventOtherPlayer"></block>
    </value>
</block>
```