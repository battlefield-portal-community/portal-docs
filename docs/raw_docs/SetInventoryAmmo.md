# %{ID_ARRIVAL_BLOCK_SETINVENTORYAMMO}

%{help.setinventoryammo.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_PLAYER}
2. %{PYRITE_TYPE_ENUM_INVENTORYSLOTS}
3. %{PYRITE_TYPE_NUMBER}

```
<block type="SetInventoryAmmo">
    <value name="VALUE-0">
        <block type="EventPlayer"></block>
    </value>
    <value name="VALUE-1">
        <block type="InventorySlotsItem">
            <field name="VALUE-0">InventorySlots</field>
            <field name="VALUE-1">SecondaryWeapon</field>
        </block>
    </value>
    <value name="VALUE-2">
        <block type="Number">
            <field name="NUM">1</field>
        </block>
    </value>
</block>
```
