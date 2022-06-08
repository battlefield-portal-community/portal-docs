# %{ID_ARRIVAL_BLOCK_NORMALIZE}

%{help.normalize.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_VECTOR}

### %{help.common.output}

-   %{PYRITE_TYPE_VECTOR}

```
<block type="Normalize">
    <value name="VALUE-0">
        <block type="GetSoldierState">
            <value name="VALUE-0">
                <block type="EventPlayer"></block>
            </value>
            <value name="VALUE-1">
                <block type="SoldierStateVectorItem">
                    <field name="VALUE-0">SoldierStateVector</field>
                    <field name="VALUE-1">GetLinearVelocity</field>
                </block>
            </value>
        </block>
    </value>
</block>
```
