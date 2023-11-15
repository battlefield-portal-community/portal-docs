# %{ID_ARRIVAL_BLOCK_ENABLEINPUTRESTRICTION}

%{help.enableinputrestriction.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_PLAYER}
2. %{PYRITE_TYPE_ENUM_RESTRICTEDINPUTS}
3. %{PYRITE_TYPE_BOOLEAN}

```
<block type="EnableInputRestriction">
    <value name="VALUE-0">
        <block type="EventPlayer"></block>
    </value>
    <value name="VALUE-1">
        <block type="RestrictedInputsItem">
            <field name="VALUE-0">RestrictedInputs</field>
            <field name="VALUE-1">FireWeapon</field>
        </block>
    </value>
    <value name="VALUE-2">
        <block type="Boolean">
            <field name="BOOL">TRUE</field>
        </block>
    </value>
</block>
```