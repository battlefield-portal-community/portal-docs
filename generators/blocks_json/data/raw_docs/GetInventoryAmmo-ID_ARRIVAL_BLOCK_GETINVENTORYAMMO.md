# %{ID_ARRIVAL_BLOCK_GETINVENTORYAMMO}

%{help.getinventoryammo.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_PLAYER}
2. %{PYRITE_TYPE_ENUM_INVENTORYSLOTS}

### %{help.common.output}

-   %{PYRITE_TYPE_NUMBER}

```
<block type="GetInventoryAmmo">
    <value name="VALUE-0">
        <block type="EventPlayer"></block>
    </value>
    <value name="VALUE-1">
        <block type="InventorySlotsItem">
            <field name="VALUE-0">InventorySlots</field>
            <field name="VALUE-1">SecondaryWeapon</field>
        </block>
    </value>
</block>
```