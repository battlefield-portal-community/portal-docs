# %{ID_ARRIVAL_BLOCK_SKIP}

%{help.skip.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_NUMBER}

```
<block type="Skip">
    <value name="VALUE-0">
        <block type="Number">
            <field name="NUM">1</field>
        </block>
    </value>
    <next>
        <block type="ShowEventGameModeMessage">
            <value name="VALUE-0">
                <block type="Message">
                    <value name="VALUE-0">
                        <block type="Text">
                            <field name="TEXT">This message will be skipped.</field>
                        </block>
                    </value>
                </block>
            </value>
        </block>
    </next>
</block>
```