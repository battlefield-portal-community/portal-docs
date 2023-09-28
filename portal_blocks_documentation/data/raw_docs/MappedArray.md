# %{ID_ARRIVAL_BLOCK_MAPPEDARRAY}

%{help.mappedarray.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_ARRAY}
2. %{PYRITE_TYPE_ANYTYPE}

    %{help.common.contexts.mapexpr}

### %{help.common.output}

-   %{PYRITE_TYPE_ARRAY}

```
<block type="MappedArray">
    <value name="VALUE-0">
        <block type="AllPlayers"></block>
    </value>
    <value name="VALUE-1">
        <block type="Subtract">
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
