# %{ID_ARRIVAL_BLOCK_MESSAGE}

%{help.message.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_STRING} | %{PYRITE_TYPE_NUMBER} | %{PYRITE_TYPE_PLAYER}
2. %{PYRITE_TYPE_STRING} | %{PYRITE_TYPE_NUMBER} | %{PYRITE_TYPE_PLAYER}

    %{help.common.optional}

3. %{PYRITE_TYPE_STRING} | %{PYRITE_TYPE_NUMBER} | %{PYRITE_TYPE_PLAYER}

    %{help.common.optional}

4. %{PYRITE_TYPE_STRING} | %{PYRITE_TYPE_NUMBER} | %{PYRITE_TYPE_PLAYER}

    %{help.common.optional}

### %{help.common.output}

-   %{PYRITE_TYPE_MESSAGE}

```
<block type="Message">
    <value name="VALUE-0">
        <block type="Text">
            <field name="TEXT">{} took the lead! They have {} points!</field>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="EventPlayer"></block>
    </value>
    <value name="VALUE-2">
        <block type="GetGamemodeScore">
            <value name="VALUE-0">
                <block type="EventPlayer"></block>
            </value>
        </block>
    </value>
</block>
```
