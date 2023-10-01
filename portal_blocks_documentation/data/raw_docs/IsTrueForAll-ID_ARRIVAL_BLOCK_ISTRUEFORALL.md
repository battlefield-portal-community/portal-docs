# %{ID_ARRIVAL_BLOCK_ISTRUEFORALL}

%{help.istrueforall.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_ARRAY}
2. %{PYRITE_TYPE_BOOLEAN}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="IsTrueForAll">
    <value name="VALUE-0">
        <block type="AllPlayers"></block>
    </value>
    <value name="VALUE-1">
        <block type="GreaterThan">
            <value name="VALUE-0">
                <block type="GetGamemodeScore">
                    <value name="VALUE-0">
                        <block type="CurrentArrayElement"></block>
                    </value>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="Number">
                    <field name="NUM">2</field>
                </block>
            </value>
        </block>
    </value>
</block>
```