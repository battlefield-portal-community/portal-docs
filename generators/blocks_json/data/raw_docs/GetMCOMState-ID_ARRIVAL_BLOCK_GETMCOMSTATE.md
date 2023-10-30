# %{ID_ARRIVAL_BLOCK_GETMCOMSTATE}

%{help.getmcomstate.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_MCOM}
2. %{PYRITE_TYPE_ENUM_MCOMSTATEBOOL}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="GetMCOMState">
    <value name="VALUE-0">
        <block type="EventMCOM"></block>
    </value>
    <value name="VALUE-1">
        <block type="MCOMStateBoolItem">
            <field name="VALUE-0">MCOMStateBool</field>
            <field name="VALUE-1">IsActive</field>
        </block>
    </value>
</block>
```