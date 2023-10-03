# %{ID_ARRIVAL_BLOCK_SETHEAL}

%{help.setheal.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_PLAYER}

    %{help.common.contexts.target}

2. %{PYRITE_TYPE_NUMBER}
3. %{PYRITE_TYPE_PLAYER}

    %{help.common.contexts.healer}

    %{help.common.optional}

```
<block type="SetHeal">
    <value name="VALUE-0">
        <block type="EventPlayer"></block>
    </value>
    <value name="VALUE-1">
        <block type="Number">
            <field name="NUM">50</field>
        </block>
    </value>
</block>
```