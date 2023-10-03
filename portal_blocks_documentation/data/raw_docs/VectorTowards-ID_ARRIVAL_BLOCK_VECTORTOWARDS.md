# %{ID_ARRIVAL_BLOCK_VECTORTOWARDS}

%{help.vectortowards.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_VECTOR}

    %{help.common.contexts.startpos}

2. %{PYRITE_TYPE_VECTOR}

    %{help.common.contexts.endpos}

### %{help.common.output}

-   %{PYRITE_TYPE_VECTOR}

```
<block type="VectorTowards">
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
        <block type="GetSoldierState">
            <value name="VALUE-0">
                <block type="EventPlayer"></block>
            </value>
            <value name="VALUE-1">
                <block type="SoldierStateVectorItem">
                    <field name="VALUE-0">SoldierStateVector</field>
                    <field name="VALUE-1">GetPosition</field>
                </block>
            </value>
        </block>
    </value>
</block>
```