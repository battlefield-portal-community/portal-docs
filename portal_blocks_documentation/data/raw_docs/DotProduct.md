# %{ID_ARRIVAL_BLOCK_DOTPRODUCT}

%{help.dotproduct.summary}

### %{help.common.input}

1. %{PYRITE_TYPE_VECTOR}
2. %{PYRITE_TYPE_VECTOR}

### %{help.common.output}

-   %{PYRITE_TYPE_NUMBER}

```
<block type="DotProduct">
    <value name="VALUE-0">
        <block type="LocalVectorOf">
            <value name="VALUE-0">
                <block type="ForwardVector"></block>
            </value>
            <value name="VALUE-1">
                <block type="EventPlayer"></block>
            </value>
        </block>
    </value>
    <value name="VALUE-1">
        <block type="LocalVectorOf">
            <value name="VALUE-0">
                <block type="ForwardVector"></block>
            </value>
            <value name="VALUE-1">
                <block type="EventOtherPlayer"></block>
            </value>
        </block>
    </value>
</block>
```
