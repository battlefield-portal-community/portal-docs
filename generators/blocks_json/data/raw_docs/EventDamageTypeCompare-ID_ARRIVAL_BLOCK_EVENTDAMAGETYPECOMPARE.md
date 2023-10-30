# %{ID_ARRIVAL_BLOCK_EVENTDAMAGETYPECOMPARE}

%{help.eventdamagetypecompare.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_DAMAGETYPE}
2. %{PYRITE_TYPE_ENUM_PLAYERDAMAGETYPES}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="EventDamageTypeCompare">
    <value name="VALUE-0">
        <block type="EventDamageType"></block>
    </value>
    <value name="VALUE-1">
        <block type="PlayerDamageTypesItem">
            <field name="VALUE-0">PlayerDamageTypes</field>
            <field name="VALUE-1">Explosion</field>
        </block>
    </value>
</block>
```