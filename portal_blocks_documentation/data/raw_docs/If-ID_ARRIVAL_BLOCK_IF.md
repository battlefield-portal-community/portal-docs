# %{ID_ARRIVAL_BLOCK_IF}

%{help.if.summary}

```
<block type="If">
    <mutation elseif="1" else="1"></mutation>
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
    <statement name="DO"></statement>
    <value name="IF1">
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
                            <field name="NUM">2</field>
                        </block>
                    </value>
                </block>
            </value>
        </block>
    </value>
    <statement name="DO1"></statement>
    <statement name="ELSE"></statement>
</block>
```