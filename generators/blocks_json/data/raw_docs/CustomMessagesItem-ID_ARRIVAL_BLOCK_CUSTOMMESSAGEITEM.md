# %{ID_ARRIVAL_BLOCK_CUSTOMMESSAGEITEM}

%{help.custommessageitem.summary}

### %{help.common.output}

-   %{PYRITE_TYPE_ENUM_CUSTOMMESSAGES}

```
<block type="DisplayCustomNotificationMessage">
    <value name="VALUE-0">
        <block type="Message">
            <value name="VALUE-0">
                <block type="Text">
                    <field name="TEXT">You picked up the item!</field>
                </block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="CustomMessagesItem">
            <field name="VALUE-0">CustomMessages</field>
            <field name="VALUE-1">MessageText1</field>
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