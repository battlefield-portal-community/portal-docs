# %{ID_ARRIVAL_BLOCK_GETVEHICLESTATE}

%{help.getvehiclestate.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_VEHICLE}
2. %{PYRITE_TYPE_ENUM_VEHICLESTATEVECTOR}

### %{help.common.output}

-   %{PYRITE_TYPE_VECTOR}

```
<block type="GetVehicleState">
    <value name="VALUE-0">
        <block type="EventVehicle"></block>
    </value>
        <value name="VALUE-1">
        <block type="VehicleStateVectorItem">
            <field name="VALUE-0">VehicleStateVector</field>
            <field name="VALUE-1">Position</field>
        </block>
    </value>
</block>
```
