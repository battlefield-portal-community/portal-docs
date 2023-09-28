# %{ID_ARRIVAL_BLOCK_HASINVENTORY}

%{help.hasinventory.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_PLAYER}
2. %{PYRITE_TYPE_ENUM_PRIMARYWEAPONS} | %{PYRITE_TYPE_ENUM_SECONDARYWEAPONS} | %{PYRITE_TYPE_ENUM_CHARACTERGADGETS} | %{PYRITE_TYPE_ENUM_OPENGADGETS} | %{PYRITE_TYPE_ENUM_CLASSGADGETS} | %{PYRITE_TYPE_ENUM_THROWABLES} | %{PYRITE_TYPE_ENUM_MELEEWEAPONS}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="HasInventory">
    <value name="VALUE-0">
        <block type="EventPlayer"></block>
    </value>
    <value name="VALUE-1">
        <block type="PrimaryWeaponsItem">
            <field name="VALUE-0">PrimaryWeaponsKingston</field>
            <field name="VALUE-1">SLX Spear</field>
        </block>
    </value>
</block>
```
