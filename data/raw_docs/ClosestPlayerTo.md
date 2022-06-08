# %{ID_ARRIVAL_BLOCK_CLOSESTPLAYERTO}

%{help.closestplayerto.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_VECTOR}

    %{help.common.contexts.position}

2. %{PYRITE_TYPE_TEAMID}

    %{help.common.optional}

### %{help.common.output}

-   %{PYRITE_TYPE_PLAYER}

```
<block type="ClosestPlayerTo">
    <value name="VALUE-0">
        <block type="CreateVector">
            <value name="VALUE-0">
                <block type="Number">
                    <field name="NUM">0</field>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="Number">
                    <field name="NUM">0</field>
                </block>
            </value>
            <value name="VALUE-2">
                <block type="Number">
                    <field name="NUM">0</field>
                </block>
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
```
