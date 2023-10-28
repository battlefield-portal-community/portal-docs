# %{ID_ARRIVAL_BLOCK_SKIPIF}

%{help.skipif.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_NUMBER}
2. %{PYRITE_TYPE_BOOLEAN}

```
<block type="SkipIf">
    <value name="VALUE-0">
        <block type="Number">
            <field name="NUM">1</field>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="Boolean">
            <field name="BOOL">TRUE</field>
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
            <next>
                <block type="ShowEventGameModeMessage">
                    <value name="VALUE-0">
                        <block type="Message">
                            <value name="VALUE-0">
                                <block type="Text">
                                    <field name="TEXT">This message will be displayed.</field>
                                </block>
                            </value>
                        </block>
                    </value>
                </block>
            </next>
        </block>
    </next>
</block>
```