# %{ID_ARRIVAL_BLOCK_GREATERTHANEQUALTO}

%{help.greaterthanequalto.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_NUMBER}
2. %{PYRITE_TYPE_NUMBER}

### %{help.common.output}

-   %{PYRITE_TYPE_BOOLEAN}

```
<block type="GreaterThanEqualTo">
    <value name="VALUE-0">
        <block type="GetGamemodeScore">
            <value name="VALUE-0">
                <block type="EventPlayer"></block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="GetTargetScore"></block>
    </value>
</block>
```