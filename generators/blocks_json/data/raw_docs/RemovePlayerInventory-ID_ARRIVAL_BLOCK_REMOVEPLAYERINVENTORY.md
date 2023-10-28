# %{ID_ARRIVAL_BLOCK_REMOVEPLAYERINVENTORY}

%{help.removeplayerinventory.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_PLAYER}
2. %{PYRITE_TYPE_ENUM_PRIMARYWEAPONS} | %{PYRITE_TYPE_ENUM_SECONDARYWEAPONS} | %{PYRITE_TYPE_ENUM_CHARACTERGADGETS} | %{PYRITE_TYPE_ENUM_OPENGADGETS} | %{PYRITE_TYPE_ENUM_CLASSGADGETS} | %{PYRITE_TYPE_ENUM_THROWABLES}

```
<block type="RemovePlayerInventory">
    <value name="VALUE-0">
        <block type="EventPlayer"></block>
    </value>
    <value name="VALUE-1">
        <block type="PrimaryWeaponsItem">
            <field name="VALUE-0">PrimaryWeaponsGrafton</field>
            <field name="VALUE-1">Bazooka</field>
        </block>
    </value>
</block>
```