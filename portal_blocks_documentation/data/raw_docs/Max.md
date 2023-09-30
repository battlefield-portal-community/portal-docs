# %{ID_ARRIVAL_BLOCK_MAX}

%{help.max.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_NUMBER}
2. %{PYRITE_TYPE_NUMBER}

### %{help.common.output}

-   %{PYRITE_TYPE_NUMBER}

```
<block type="Max">
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
            <field name="NUM">50</field>
        </block>
    </value>
</block>
```
