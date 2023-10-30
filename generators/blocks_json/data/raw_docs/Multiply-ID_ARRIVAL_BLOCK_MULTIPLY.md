# %{ID_ARRIVAL_BLOCK_MULTIPLY}

%{help.multiply.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_NUMBER} | %{PYRITE_TYPE_VECTOR}
2. %{PYRITE_TYPE_NUMBER}

### %{help.common.output}

-   %{PYRITE_TYPE_NUMBER} | %{PYRITE_TYPE_VECTOR}

```
<block type="Multiply">
    <value name="VALUE-0">
        <block type="GetSoldierState">
            <value name="VALUE-0">
                <block type="EventPlayer"></block>
            </value>
            <value name="VALUE-1">
                <block type="SoldierStateNumberItem">
                    <field name="VALUE-0">SoldierStateNumber</field>
                    <field name="VALUE-1">CurrentHealth</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="Number">
            <field name="NUM">5</field>
        </block>
    </value>
</block>
```