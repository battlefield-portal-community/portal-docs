# %{ID_ARRIVAL_BLOCK_GREATERTHAN}

%{help.greaterthan.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_NUMBER}
2. %{PYRITE_TYPE_NUMBER}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="GreaterThan">
    <value name="VALUE-0">
        <block type="GetGamemodeScore">
            <value name="VALUE-0">
                <block type="EventPlayer"></block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="Number">
            <field name="NUM">10</field>
        </block>
    </value>
</block>
```
