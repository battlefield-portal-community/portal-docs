# %{ID_ARRIVAL_BLOCK_SETWORLDICONPOSITION}

%{help.setworldiconposition.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_ENUM_WORLDICONS}
2. %{PYRITE_TYPE_VECTOR}

```
<block type="SetWorldIconPosition">
    <value name="VALUE-0">
        <block type="WorldIconsItem">
            <field name="VALUE-0">WorldIcons</field>
            <field name="VALUE-1">B</field>
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
