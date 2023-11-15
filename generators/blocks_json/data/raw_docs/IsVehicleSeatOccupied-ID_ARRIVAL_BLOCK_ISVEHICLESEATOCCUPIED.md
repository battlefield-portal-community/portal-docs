# %{ID_ARRIVAL_BLOCK_ISVEHICLESEATOCCUPIED}

%{help.isvehicleseatoccupied.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_VEHICLE}

2. %{PYRITE_TYPE_NUMBER}

### %{help.common.output}

1. %{PYRITE_TYPE_BOOLEAN}

```
<block type="IsVehicleSeatOccupied">
    <value name="VALUE-0">
        <block type="EventVehicle"></block>
    </value>
    <value name="VALUE-1">
        <block type="Number">
            <field name="NUM">1</field>
        </block>
    </value>
</block>
```