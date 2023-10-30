# %{ID_ARRIVAL_BLOCK_CROSSPRODUCT}

%{help.crossproduct.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_VECTOR}
2. %{PYRITE_TYPE_VECTOR}

### %{help.common.output}

-   %{PYRITE_TYPE_VECTOR}

```
<block type="CrossProduct">
    <value name="VALUE-0">
        <block type="CreateVector">
            <value name="VALUE-0">
                <block type="Number">
                    <field name="NUM">3</field>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="Number">
                    <field name="NUM">5</field>
                </block>
            </value>
            <value name="VALUE-2">
                <block type="Number">
                    <field name="NUM">6</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="ForwardVector">
        </block>
    </value>
</block>
```