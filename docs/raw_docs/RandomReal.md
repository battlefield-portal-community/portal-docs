# %{ID_ARRIVAL_BLOCK_RANDOMREAL}

%{help.randomreal.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_NUMBER}

    %{help.common.contexts.min}

2. %{PYRITE_TYPE_NUMBER}

    %{help.common.contexts.max}

### %{help.common.output}

-   %{PYRITE_TYPE_NUMBER}

```
<block type="RandomReal">
    <value name="VALUE-0">
        <block type="Number">
            <field name="NUM">0</field>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="Subtract">
            <value name="VALUE-0">
                <block type="CountOf">
                    <value name="VALUE-0">
                        <block type="AllPlayers"></block>
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
</block>
```
