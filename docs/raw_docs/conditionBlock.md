# %{PYRITE_CONDITION}

%{help.condition.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_BOOLEAN}

```
<block type="ruleBlock">
    <mutation isOnGoingEvent="false"></mutation>
    <field name="NAME">New Rule</field>
    <field name="EVENTTYPE">OnPlayerEarnedKill</field>
    <statement name="CONDITIONS">
        <block type="conditionBlock">
            <value name="CONDITION">
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
    <statement name="ACTIONS">
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
                        <block type="Number">npm start
                            <field name="NUM">1</field>
                        </block>
                    </value>
                </block>
            </value>
        </block>
    </statement>
</block>
```
