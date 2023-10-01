# %{ID_ARRIVAL_BLOCK_ABORTIF}

%{help.abortif.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_BOOLEAN}

```
<block type="ruleBlock">
    <mutation isOnGoingEvent="false"></mutation>
    <field name="NAME">New Rule</field>
    <field name="EVENTTYPE">OnPlayerEarnedKill</field>
    <statement name="CONDITIONS"></statement>
    <statement name="ACTIONS">
        <block type="AbortIf">
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
        </block>
    </statement>
</block>
```