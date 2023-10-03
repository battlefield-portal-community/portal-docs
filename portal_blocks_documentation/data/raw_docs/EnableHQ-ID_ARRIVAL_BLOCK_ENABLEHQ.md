# %{ID_ARRIVAL_BLOCK_ENABLEHQ}

%{help.enablehq.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_TEAMID}
2. %{PYRITE_TYPE_NUMBER}

    %{help.common.contexts.index}

3. %{PYRITE_TYPE_BOOLEAN}

```
<block type="EnableHQ">
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
        <block type="Number">
            <field name="NUM">0</field>
        </block>
    </value>
    <value name="VALUE-2">
        <block type="Boolean">
            <field name="BOOL">FALSE</field>
        </block>
    </value>
</block>
```