# %{ID_ARRIVAL_BLOCK_SENDERRORREPORT}

%{help.senderrorreport.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_MESSAGE}

```
<block type="SendErrorReport">
    <value name="VALUE-0">
        <block type="Message">
            <value name="VALUE-0">
                <block type="Text">
                    <field name="TEXT">{} is out of bounds on the map!</field>
                </block>
            </value>
            <value name="VALUE-1">
                <block type="EventPlayer"></block>
            </value>
        </block>
    </value>
</block>
```
