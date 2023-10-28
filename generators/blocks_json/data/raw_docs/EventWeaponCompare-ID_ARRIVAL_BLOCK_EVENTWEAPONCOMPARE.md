# %{ID_ARRIVAL_BLOCK_EVENTWEAPONCOMPARE}

%{help.eventweaponcompare.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_HARDWAREID}
2. %{PYRITE_TYPE_ENUM_PRIMARYWEAPONS} | %{PYRITE_TYPE_ENUM_SECONDARYWEAPONS} | %{PYRITE_TYPE_ENUM_CHARACTERGADGETS} | %{PYRITE_TYPE_ENUM_OPENGADGETS} | %{PYRITE_TYPE_ENUM_CLASSGADGETS} | %{PYRITE_TYPE_ENUM_THROWABLES} | %{PYRITE_TYPE_ENUM_MELEEWEAPONS}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="EventWeaponCompare">
    <value name="VALUE-0">
        <block type="EventWeapon"></block>
    </value>
    <value name="VALUE-1">
        <block type="PrimaryWeaponsItem">
            <field name="VALUE-0">PrimaryWeaponsGrafton</field>
            <field name="VALUE-1">Bazooka</field>
        </block>
    </value>
</block>
```