# %{ID_ARRIVAL_BLOCK_LOCALPOSITIONOF}

%{help.localpositionof.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_VECTOR}

    %{help.common.contexts.worldpos}

2. %{PYRITE_TYPE_PLAYER}

### %{help.common.output}

-   %{PYRITE_TYPE_VECTOR}

    %{help.common.contexts.localpos}

```
<block type="LocalPositionOf">
    <value name="VALUE-0">
        <block type="CreateVector">
            <value name="VALUE-0">
                <block type="Number">
                    <field name="NUM">0</field>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="Number">
                    <field name="NUM">0</field>
                </block>
            </value>
            <value name="VALUE-2">
                <block type="Number">
                    <field name="NUM">0</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="EventPlayer"></block>
    </value>
</block>
```
