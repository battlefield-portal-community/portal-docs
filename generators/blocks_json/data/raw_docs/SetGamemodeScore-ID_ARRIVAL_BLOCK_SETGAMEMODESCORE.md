# %{ID_ARRIVAL_BLOCK_SETGAMEMODESCORE}

%{help.setgamemodescore.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_PLAYER} | %{PYRITE_TYPE_TEAMID}
2. %{PYRITE_TYPE_NUMBER}

```
<block type="SetGamemodeScore">
    <value name="VALUE-0">
        <block type="EventPlayer"></block>
    </value>
    <value name="VALUE-1">
        <block type="Add">
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
</block>
```