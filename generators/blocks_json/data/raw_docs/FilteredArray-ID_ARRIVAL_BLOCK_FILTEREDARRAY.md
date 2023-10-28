# %{ID_ARRIVAL_BLOCK_FILTEREDARRAY}

%{help.filteredarray.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_ARRAY}
2. %{PYRITE_TYPE_ANYTYPE}

### %{help.common.output}

-   %{PYRITE_TYPE_ARRAY}

```
<block type="FilteredArray">
    <value name="VALUE-0">
        <block type="AllPlayers"></block>
    </value>
    <value name="VALUE-1">
        <block type="Equals">
            <value name="VALUE-0">
                <block type="GetTeamId">
                    <value name="VALUE-0">
                        <block type="Number">
                            <field name="NUM">1</field>
                        </block>
                    </value>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="GetTeamId">
                    <value name="VALUE-0">
                        <block type="CurrentArrayElement"></block>
                    </value>
                </block>
            </value>
        </block>
    </value>
</block>
```