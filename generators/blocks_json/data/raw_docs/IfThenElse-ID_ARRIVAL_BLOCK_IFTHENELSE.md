# %{ID_ARRIVAL_BLOCK_IFTHENELSE}

%{help.ifthenelse.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_BOOLEAN}
2. %{PYRITE_TYPE_ANYTYPE}

    %{help.common.contexts.outputtrue}

3. %{PYRITE_TYPE_ANYTYPE}

    %{help.common.contexts.outputfalse}

### %{help.common.output}

-   %{PYRITE_TYPE_ANYTYPE}

```
<block type="IfThenElse">
    <value name="VALUE-0">
        <block type="Equals">
            <value name="VALUE-0">
                <block type="GetTeamId">
                    <value name="VALUE-0">
                        <block type="EventPlayer"></block>
                    </value>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="GetTeamId">
                    <value name="VALUE-0">
                        <block type="Number">
                            <field name="NUM">1</field>
                        </block>
                    </value>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="Number">
            <field name="NUM">10</field>
        </block>
    </value>
    <value name="VALUE-2">
        <block type="Number">
            <field name="NUM">0</field>
        </block>
    </value>
</block>
```