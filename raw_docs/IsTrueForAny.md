# %{ID_ARRIVAL_BLOCK_ISTRUEFORANY}

%{help.istrueforany.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_ARRAY}
2. %{PYRITE_TYPE_BOOLEAN}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="IsTrueForAny">
    <value name="VALUE-0">
        <block type="AllPlayers"></block>
    </value>
    <value name="VALUE-1">
        <block type="Equals">
            <value name="VALUE-0">
                <block type="GetPlayerDeaths">
                    <value name="VALUE-0">
                        <block type="CurrentArrayElement"></block>
                    </value>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="Number">
                    <field name="NUM">10</field>
                </block>
            </value>
        </block>
    </value>
</block>
```
