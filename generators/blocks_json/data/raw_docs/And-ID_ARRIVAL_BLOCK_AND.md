# %{ID_ARRIVAL_BLOCK_AND}

%{help.and.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_BOOLEAN}
2. %{PYRITE_TYPE_BOOLEAN}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="And">
    <value name="VALUE-0">
        <block type="GreaterThan">
            <value name="VALUE-0">
                <block type="GetGamemodeScore">
                    <value name="VALUE-0">
                        <block type="EventPlayer"></block>
                    </value>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="Number">
                    <field name="NUM">1</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="LessThan">
            <value name="VALUE-0">
                <block type="GetGamemodeScore">
                    <value name="VALUE-0">
                        <block type="EventPlayer"></block>
                    </value>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="Number">
                    <field name="NUM">4</field>
                </block>
            </value>
        </block>
    </value>
</block>
```