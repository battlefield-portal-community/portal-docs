# %{ID_ARRIVAL_BLOCK_WAITUNTIL}

%{help.waituntil.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_NUMBER}
2. %{PYRITE_TYPE_BOOLEAN}

## %{help.common.output}

```
<block type="WaitUntil">
    <value name="VALUE-0">
        <block type="Number">
            <field name="NUM">5</field>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="GetSoldierState">
            <value name="VALUE-0">
                <block type="EventPlayer"></block>
            </value>
            <value name="VALUE-1">
                <block type="SoldierStateBoolItem">
                    <field name="VALUE-0">SoldierStateBool</field>
                    <field name="VALUE-1">IsInAir</field>
                </block>
            </value>
        </block>
    </value>
</block>
```
