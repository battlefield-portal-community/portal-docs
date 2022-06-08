# %{ID_ARRIVAL_BLOCK_GETSOLDIERSTATE}

%{help.getsoldierstate.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_PLAYER}
2. %{PYRITE_TYPE_ENUM_SOLDIERSTATEBOOL} | %{PYRITE_TYPE_ENUM_SOLDIERSTATENUMBER} | %{PYRITE_TYPE_ENUM_SOLDIERSTATEVECTOR}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN} | %{PYRITE_TYPE_NUMBER} | %{PYRITE_TYPE_VECTOR}

```
<block type="GetSoldierState">
    <value name="VALUE-0">
        <block type="EventPlayer"></block>
    </value>
        <value name="VALUE-1">
        <block type="SoldierStateBoolItem">
            <field name="VALUE-0">SoldierStateBool</field>
            <field name="VALUE-1">IsAISoldier</field>
        </block>
    </value>
</block>
```
