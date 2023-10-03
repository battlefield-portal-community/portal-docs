# %{ID_ARRIVAL_BLOCK_COMPAREVEHICLENAME}

%{help.comparevehiclename.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_VEHICLE}
2. %{PYRITE_TYPE_ENUM_VEHICLES} | %{PYRITE_TYPE_ENUM_VEHICLETYPES}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="CompareVehicleName">
    <value name="VALUE-0">
        <block type="EventVehicle"></block>
    </value>
    <value name="VALUE-1">
        <block type="VehiclesItem">
            <field name="VALUE-0">Heavy</field>
            <field name="VALUE-1">T90</field>
        </block>
    </value>
</block>
```