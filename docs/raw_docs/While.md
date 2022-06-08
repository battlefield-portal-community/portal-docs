# %{ID_ARRIVAL_BLOCK_WHILE}

%{help.while.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_BOOLEAN}

```
<block type="While">
    <value name="VALUE-0">
        <block type="GetSoldierState">
            <value name="VALUE-0">
                <block type="EventPlayer"></block>
            </value>
            <value name="VALUE-1">
                <block type="SoldierStateBoolItem">
                    <field name="VALUE-0">SoldierStateBool</field>
                    <field name="VALUE-1">IsAlive</field>
                </block>
            </value>
        </block>
    </value>
    <statement name="DO">
        <block type="Wait">
            <value name="VALUE-0">
                <block type="Number">
                    <field name="NUM">1</field>
                </block>
            </value>
        </block>
    </statement>
</block>
```
