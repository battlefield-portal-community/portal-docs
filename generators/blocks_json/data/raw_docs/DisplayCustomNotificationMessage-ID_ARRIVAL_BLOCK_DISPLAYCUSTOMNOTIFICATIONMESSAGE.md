# %{ID_ARRIVAL_BLOCK_DISPLAYCUSTOMNOTIFICATIONMESSAGE}

%{help.displaycustommessage.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_MESSAGE}
2. %{PYRITE_TYPE_ENUM_CUSTOMMESSAGES}
3. %{PYRITE_TYPE_NUMBER}

    %{help.common.contexts.duration}

4. %{PYRITE_TYPE_PLAYER} | %{PYRITE_TYPE_TEAMID}

    %{help.common.contexts.group}

    %{help.common.optional}

```
<block type="DisplayCustomNotificationMessage">
    <value name="VALUE-0">
        <block type="Message">
            <value name="VALUE-0">
                <block type="Text">
                    <field name="TEXT">This is a Custom Message!</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="CustomMessagesItem">
            <field name="VALUE-0">CustomMessages</field>
            <field name="VALUE-1">HeaderText</field>
        </block>
    </value>
    <value name="VALUE-2">
        <block type="Number">
            <field name="NUM">-1</field>
        </block>
    </value>
    <value name="VALUE-3">
        <block type="EventPlayer"></block>
    </value>
</block>
```