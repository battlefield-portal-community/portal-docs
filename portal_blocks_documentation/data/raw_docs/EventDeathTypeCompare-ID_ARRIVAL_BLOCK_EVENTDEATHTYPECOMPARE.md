# %{ID_ARRIVAL_BLOCK_EVENTDEATHTYPECOMPARE}

%{help.eventdeathtypecompare.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_DEATHTYPE}
2. %{PYRITE_TYPE_ENUM_PLAYERDEATHTYPES}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="EventDeathTypeCompare">
    <value name="VALUE-0">
        <block type="EventDeathType"></block>
    </value>
    <value name="VALUE-1">
        <block type="PlayerDeathTypesItem">
            <field name="VALUE-0">PlayerDeathTypes</field>
            <field name="VALUE-1">Headshot</field>
        </block>
    </value>
</block>
```