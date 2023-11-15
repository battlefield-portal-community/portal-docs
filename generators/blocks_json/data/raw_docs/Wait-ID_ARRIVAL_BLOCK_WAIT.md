# %{ID_ARRIVAL_BLOCK_WAIT}

%{help.wait.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_NUMBER}

```
<block type="Wait">
    <value name="VALUE-0">
        <block type="Number">
            <field name="NUM">6</field>
        </block>
    </value>
    <next>
        <block type="ShowEventGameModeMessage">
            <value name="VALUE-0">
                <block type="Message">
                    <value name="VALUE-0">
                        <block type="Text">
                            <field name="TEXT">This message will be displayed 6 seconds later.</field>
                        </block>
                    </value>
                </block>
            </value>
        </block>
    </next>
</block>
```