# %{ID_ARRIVAL_BLOCK_SHOWEVENTGAMEMODEMESSAGE}

%{help.showgamemodemessage.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_MESSAGE}
2. %{PYRITE_TYPE_PLAYER} | %{PYRITE_TYPE_TEAMID}

    %{help.common.optional}

```
<block type="ShowEventGameModeMessage">
    <value name="VALUE-0">
        <block type="Message">
            <value name="VALUE-0">
                <block type="Text">
                    <field name="TEXT">Hello World!</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="EventPlayer"></block>
    </value>
</block>
```