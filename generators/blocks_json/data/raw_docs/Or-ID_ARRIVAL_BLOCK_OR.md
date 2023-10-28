# %{ID_ARRIVAL_BLOCK_OR}

%{help.or.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_BOOLEAN}
2. %{PYRITE_TYPE_BOOLEAN}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="Or">
    <value name="VALUE-0">
        <block type="GreaterThanEqualTo">
            <value name="VALUE-0">
                <block type="GetGamemodeScore">
                    <value name="VALUE-0">
                        <block type="EventPlayer"></block>
                    </value>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="Number">
                    <field name="NUM">25</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="LessThanEqualTo">
            <value name="VALUE-0">
                <block type="GetGamemodeScore">
                    <value name="VALUE-0">
                        <block type="EventOtherPlayer"></block>
                    </value>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="Number">
                    <field name="NUM">0</field>
                </block>
            </value>
        </block>
    </value>
</block>
```